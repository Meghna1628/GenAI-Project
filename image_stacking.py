import cv2
import os
import numpy as np

def add_label(frame, label):
    """Overlay label (e.g., filename) on the frame with larger text."""
    font = cv2.FONT_HERSHEY_SIMPLEX
    font_scale = 2  # Increased for bigger text
    color = (255, 255, 255)  # White text
    thickness = 4  # Thicker text

    text_size = cv2.getTextSize(label, font, font_scale, thickness)[0]
    text_x = 20
    text_y = text_size[1] + 30  # Position lower for visibility
    padding = 20

    box_start = (text_x - padding, text_y - text_size[1] - padding)
    box_end = (text_x + text_size[0] + padding, text_y + padding)

    # Draw semi-transparent black background
    overlay = frame.copy()
    cv2.rectangle(overlay, box_start, box_end, (0, 0, 0), -1)
    cv2.addWeighted(overlay, 0.5, frame, 0.5, 0, frame)

    # Put the label text
    cv2.putText(frame, label, (text_x, text_y), font, font_scale, color, thickness, cv2.LINE_AA)
    cv2.rectangle(frame, box_start, box_end, (0, 0, 255), 3)  # Optional red outline

    return frame


def add_frame_border(frame, border_thickness=5):
    """Adds a white border around each frame."""
    border_color = (255, 255, 255)
    return cv2.copyMakeBorder(frame, border_thickness, border_thickness, border_thickness, border_thickness,
                               cv2.BORDER_CONSTANT, value=border_color)

def stack_frames_from_folder(frames_folder, output_image_path):
    # Gather and sort image filenames
    frame_files = sorted([
        f for f in os.listdir(frames_folder)
        if f.lower().endswith(('.jpg', '.jpeg', '.png'))
    ])

    if not frame_files:
        print("❌ No image frames found in folder.")
        return

    stacked_frames = []

    for filename in frame_files:
        image_path = os.path.join(frames_folder, filename)
        frame = cv2.imread(image_path)

        if frame is None:
            print(f"⚠️ Skipping invalid image: {filename}")
            continue

        # Add filename label and border
        frame = add_label(frame, os.path.splitext(filename)[0])
        frame = add_frame_border(frame)
        stacked_frames.append(frame)

    # Resize all frames to the same width
    frame_width = min(f.shape[1] for f in stacked_frames)
    resized_frames = [
        cv2.resize(f, (frame_width, int(f.shape[0] * (frame_width / f.shape[1]))))
        for f in stacked_frames
    ]

    # Stack vertically
    stacked_image = np.vstack(resized_frames)
    cv2.imwrite(output_image_path, stacked_image)
    print(f"✅ Stacked image saved at: {output_image_path}")

    return output_image_path

# === USAGE ===
frames_folder = "/Users/meghnareddy/Desktop/LLM_Project/src/data/video10/frames"  # Replace with your folder path
output_image_path = "/Users/meghnareddy/Desktop/LLM_Project/src/data/video10/stacked_frames.jpg"

stack_frames_from_folder(frames_folder, output_image_path)
