import os
import json
from PIL import Image
import torch
from transformers import DetrFeatureExtractor, DetrForSegmentation

# Initialize the processor and model for object detection
feature_extractor = DetrFeatureExtractor.from_pretrained("facebook/detr-resnet-50-panoptic")
model = DetrForSegmentation.from_pretrained("facebook/detr-resnet-50-panoptic")

# Path to your frames folder
frames_folder = "/src/data/video10/frames" 
output_json = "/src/data/video10/object_segmentation.json" 

# Dictionary to store the results
objects_detected = {}

# Process each image in the folder
for filename in sorted(os.listdir(frames_folder)):
    if filename.lower().endswith(('.jpg', '.jpeg', '.png')):
        image_path = os.path.join(frames_folder, filename)
        try:
            # Open the image and process it with the model
            image = Image.open(image_path).convert("RGB")
            inputs = feature_extractor(images=image, return_tensors="pt")
            with torch.no_grad():
                outputs = model(**inputs)
            
            # Post-process the segmentation results
            processed_sizes = torch.as_tensor(inputs["pixel_values"].shape[-2:]).unsqueeze(0)
            result = feature_extractor.post_process_panoptic(outputs, processed_sizes)[0]
            segments_info = result["segments_info"]

            # Extract the object labels
            id2label = model.config.id2label
            detected_labels = set()

            for segment in segments_info:
                category_id = segment.get("category_id", None)
                label_id = segment.get("label_id", None)

                # We prioritize category_id, but if not available, use label_id
                label = None
                if category_id is not None:
                    label = id2label.get(category_id, f"Unknown category_{category_id}")
                elif label_id is not None:
                    label = id2label.get(label_id, f"Unknown label_{label_id}")

                if label:
                    detected_labels.add(label)

            # Save the detected objects for this image
            objects_detected[filename] = list(detected_labels)
            print(f" {filename}: {', '.join(detected_labels)}")

        except Exception as e:
            print(f" Failed to process {filename}: {e}")

# Save the results to a JSON file
with open(output_json, 'w') as f:
    json.dump(objects_detected, f, indent=4)

print(f"\n Object detection results saved to '{output_json}'")
