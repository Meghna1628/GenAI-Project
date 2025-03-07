import cv2
import numpy as np

def add_timestamp(frame, text, frame_number):
    """Overlay timestamp on the frame."""
    font = cv2.FONT_HERSHEY_SIMPLEX
    font_scale = 1
    color = (255, 255, 255)  # White text
    thickness = 2

    # full_text = f"Frame: {frame_number} | {text}"

    # Get text size for positioning
    text_size = cv2.getTextSize(text, font, font_scale, thickness)[0]
    text_x = 10
    text_y = text_size[1] + 10  # Position at top-left corner
    padding = 10  
    box_start = (text_x - padding, text_y - text_size[1] - padding)
    box_end = (text_x + text_size[0] + padding, text_y + padding)
    border_color = (0, 0, 255)

    # Draw a filled rectangle for text background
    cv2.rectangle(frame, box_start, box_end, (0, 0, 0), -1)  # Solid black box

    # Add a semi-transparent background for better visibility
    overlay = frame.copy()
    cv2.rectangle(overlay, (text_x - 5, text_y - text_size[1] - 5), (text_x + text_size[0] + 5, text_y + 5), (0, 0, 0), -1)
    cv2.addWeighted(overlay, 0.5, frame, 0.5, 0, frame)

    # Put the timestamp text
    cv2.putText(frame, text, (text_x, text_y), font, font_scale, color, thickness, cv2.LINE_AA)
    cv2.rectangle(frame, box_start, box_end, border_color, 2)

    return frame

def add_frame_border(frame, border_thickness=5):
    """Adds a white border around each frame for differentiation."""
    border_color = (255, 255, 255)  # White border
    return cv2.copyMakeBorder(frame, border_thickness, border_thickness, border_thickness, border_thickness, cv2.BORDER_CONSTANT, value=border_color)

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
        
        # Calculate timestamp in milliseconds
        timestamp_ms = int((frame_idx / fps) * 100)
        timestamp_text = f"{int(timestamp_ms // 6000):02d}:{int((timestamp_ms % 6000) // 100):02d}:{timestamp_ms % 100:02d}"


        # Add timestamp to the frame
        frame = add_timestamp(frame, timestamp_text, frame_idx)

        # Add white border around the frame
        frame = add_frame_border(frame)

        selected_frames.append(frame)
        frame_idx += frame_interval

    cap.release()

    if not selected_frames:
        print("Error: No frames were extracted.")
        return

    # Resize frames for uniform height
    frame_width = min(f.shape[1] for f in selected_frames)
    resized_frames = [cv2.resize(f, (frame_width, int(f.shape[0] * (frame_width / f.shape[1])))) for f in selected_frames]

    # Stack frames horizontally
    stacked_image = np.vstack(resized_frames)

    # Save the output image
    cv2.imwrite(output_image_path, stacked_image)

    return output_image_path

video_path = "/AwkwardWillFerrellGIFbySaturdayNightLive-ezgif.com-gif-to-mp4-converter.mp4"
output_image_path = "vertically_stacked_image.jpg"

# Convert video to stacked image
image_path = video_to_stacked_image(video_path, output_image_path)

if not image_path:
    print("Error: Image generation failed.")
    exit()