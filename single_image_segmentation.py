
import io
import os
from PIL import Image
import torch
import numpy as np
import matplotlib.pyplot as plt

from transformers import DetrFeatureExtractor, DetrForSegmentation
from transformers.models.detr.feature_extraction_detr import rgb_to_id

# === Step 1: Load Local Image ===
image_path = "/src/data/video1/frames/frame_0000.jpg"  # Replace with your image path
assert os.path.exists(image_path), f"Image not found: {image_path}"
image = Image.open(image_path).convert("RGB")

# === Step 2: Load Feature Extractor and Model ===
feature_extractor = DetrFeatureExtractor.from_pretrained("facebook/detr-resnet-50-panoptic")
model = DetrForSegmentation.from_pretrained("facebook/detr-resnet-50-panoptic")

# === Step 3: Prepare Input and Run Model ===
inputs = feature_extractor(images=image, return_tensors="pt")
with torch.no_grad():
    outputs = model(**inputs)

# === Step 4: Post-process Panoptic Segmentation ===
processed_sizes = torch.as_tensor(inputs["pixel_values"].shape[-2:]).unsqueeze(0)
result = feature_extractor.post_process_panoptic(outputs, processed_sizes)[0]

# === Step 5: Decode PNG-encoded segmentation map ===
panoptic_seg = Image.open(io.BytesIO(result["png_string"]))
panoptic_seg = np.array(panoptic_seg, dtype=np.uint8)
panoptic_seg_id = rgb_to_id(panoptic_seg)

# === Step 6: Get id2label from model config ===
id2label = model.config.id2label

# === Step 7: Visualize if segments exist ===
segments_info = result["segments_info"]

if not segments_info:
    print("❌ No objects detected.")
else:
    # Color map
    import random
    id2color = {segment["id"]: [random.randint(0, 255) for _ in range(3)] for segment in segments_info}
    
    # Create RGB mask
    seg_colored = np.zeros((panoptic_seg.shape[0], panoptic_seg.shape[1], 3), dtype=np.uint8)
    for segment in segments_info:
        seg_colored[panoptic_seg_id == segment["id"]] = id2color[segment["id"]]
    
    # Display images
    plt.figure(figsize=(12, 6))
    plt.subplot(1, 2, 1)
    plt.imshow(image)
    plt.title("Original Image")
    plt.axis("off")

    plt.subplot(1, 2, 2)
    plt.imshow(seg_colored)
    plt.title("Panoptic Segmentation (Color Encoded)")
    plt.axis("off")
    plt.show()

    # Print object list
    print("\nObjects detected in the image:")
    detected_labels = set()

    for segment in segments_info:
        label_id = segment.get("category_id", segment.get("label_id"))  # handle both keys
        label = id2label.get(label_id, f"label_{label_id}")
        detected_labels.add(label)

    for label in sorted(detected_labels):
        print(f" - {label}")

