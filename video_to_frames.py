import cv2
import os

def extract_frames(video_path, output_folder, frame_rate):
    os.makedirs(output_folder, exist_ok=True)

    cap = cv2.VideoCapture(video_path)
    total_frames = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
    fps = cap.get(cv2.CAP_PROP_FPS)

    print(f"Total Frames: {total_frames}, FPS: {fps}")

    count = 0
    saved = 0

    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            break

        if count % int(fps // frame_rate) == 0:
            filename = os.path.join(output_folder, f"frame_{saved:04d}.jpg")
            cv2.imwrite(filename, frame)
            saved += 1

        count += 1

    cap.release()
    print(f"Saved {saved} frames to '{output_folder}'")

# Example usage
extract_frames("/src/data/video10/cooking10.mp4", "/Users/meghnareddy/Desktop/LLM_Project/src/data/video10/frames", frame_rate=0.2)  
