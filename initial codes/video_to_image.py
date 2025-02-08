import cv2
import numpy as np
from PIL import Image

def video_to_stacked_image(video_path, output_image_path, frame_interval=None, max_frames=10):
    cap = cv2.VideoCapture(video_path)

    if not cap.isOpened():
        print("Error: Could not open video.")
        return

    total_frames = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
    fps = cap.get(cv2.CAP_PROP_FPS)
    
    # Auto-adjust frame interval for short videos
    if frame_interval is None:
        frame_interval = max(1, total_frames // max_frames)  # Ensure enough frames

    selected_frames = []
    frame_idx = 0

    while len(selected_frames) < max_frames and frame_idx < total_frames:
        cap.set(cv2.CAP_PROP_POS_FRAMES, frame_idx)
        ret, frame = cap.read()

        if not ret:
            break

        selected_frames.append(frame)
        frame_idx += frame_interval

    cap.release()

    if not selected_frames:
        print("Error: No frames were extracted.")
        return

    # Resize frames for uniform height
    frame_height = min(f.shape[0] for f in selected_frames)
    resized_frames = [cv2.resize(f, (int(f.shape[1] * (frame_height / f.shape[0])), frame_height)) for f in selected_frames]

    # Stack frames horizontally
    stacked_image = np.hstack(resized_frames)

    # Save the output image
    cv2.imwrite(output_image_path, stacked_image)

    return output_image_path