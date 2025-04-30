import os
import json
from transformers import BlipProcessor, BlipForConditionalGeneration
from PIL import Image

# Load model and processor
processor = BlipProcessor.from_pretrained("Salesforce/blip-image-captioning-large")
model = BlipForConditionalGeneration.from_pretrained("Salesforce/blip-image-captioning-large")

# Path to your frames folder
frames_folder = "/src/data/video10/frames"

# Output JSON file
output_json = "/src/data/video10/captions.json"
captions = {}

# Loop over all frame images
for filename in sorted(os.listdir(frames_folder)):
    if filename.lower().endswith(('.jpg', '.jpeg', '.png')):
        image_path = os.path.join(frames_folder, filename)
        try:
            image = Image.open(image_path).convert("RGB")
            inputs = processor(image, return_tensors="pt")
            out = model.generate(**inputs)
            caption = processor.decode(out[0], skip_special_tokens=True)
            captions[filename] = caption
            print(f"{filename}: {caption}")
        except Exception as e:
            print(f" Failed to process {filename}: {e}")

# Save to JSON file
with open(output_json, 'w') as f:
    json.dump(captions, f, indent=4)

print(f"\n📝 Captions saved to '{output_json}'")
