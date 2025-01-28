import cv2
import os

# Replace 'your_video.mp4' with the path to your video file
video_path = '/Users/vishnu/Desktop/MusicDanceProject/animations/mp4/listening.mp4'
cap = cv2.VideoCapture(video_path)

frame_rate = 30  # Assuming 30 frames per second of video

# Create the directory if it doesn't exist
animations_folder = 'animations/listening'
if not os.path.exists(animations_folder):
    os.makedirs(animations_folder)

frame_count = 0

while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break

    # Save every frame
    frame_path = os.path.join(animations_folder, f'frame_{frame_count}.png')
    cv2.imwrite(frame_path, frame)
    
    frame_count += 1

cap.release()
cv2.destroyAllWindows()
