import cv2
import mediapipe as mp
from mediapipe.tasks import python
from mediapipe.tasks.python import vision
import pyautogui
import os
import urllib.request
import numpy as np

MODEL_URL = 'https://storage.googleapis.com/mediapipe-models/hand_landmarker/hand_landmarker/float16/1/hand_landmarker.task'
MODEL_PATH = 'hand_landmarker.task'

if not os.path.exists(MODEL_PATH):
    print(f"Downloading MediaPipe Hand Landmarker model ({MODEL_PATH})...")
    urllib.request.urlretrieve(MODEL_URL, MODEL_PATH)
    print("Download complete!")

cam = cv2.VideoCapture(0)

base_options = python.BaseOptions(model_asset_path=MODEL_PATH)
options = vision.HandLandmarkerOptions(
    base_options=base_options,
    num_hands=1,
    min_hand_detection_confidence=0.7,
    min_hand_presence_confidence=0.7,
    min_tracking_confidence=0.7
)

detector = vision.HandLandmarker.create_from_options(options)
screen_width, screen_height = pyautogui.size()
index_y = 0
thumb_y = 0

print("Starting Virtual Mouse... Press 'q' in the camera window to quit.")

while True:
    success, frame = cam.read()
    if not success:
        print("Membaca frame webcam gagal!")
        break
    
    # Flip the frame horizontally to display like a mirror
    frame = cv2.flip(frame, 1)
    frame_height, frame_width, _ = frame.shape
    
    # Process RGB frame
    rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    mp_image = mp.Image(image_format=mp.ImageFormat.SRGB, data=rgb_frame)
    
    detection_result = detector.detect(mp_image)
    
    if detection_result.hand_landmarks:
        for hand_landmarks in detection_result.hand_landmarks:
            for id, landmark in enumerate(hand_landmarks):
                x = int(landmark.x * frame_width)
                y = int(landmark.y * frame_height)
                
                # Draw tiny dots for all landmarks
                cv2.circle(img=frame, center=(x, y), radius=3, color=(0, 255, 0), thickness=-1)
                
                # Index finger tip is 8
                if id == 8:
                    cv2.circle(img=frame, center=(x, y), radius=10, color=(0, 255, 255), thickness=-1)
                    index_x = screen_width / frame_width * x
                    index_y = screen_height / frame_height * y
                    
                    try:
                        pyautogui.moveTo(int(index_x), int(index_y))
                    except Exception as e:
                        pass
                
                # Thumb tip is 4
                if id == 4:
                    cv2.circle(img=frame, center=(x, y), radius=10, color=(0, 255, 255), thickness=-1)
                    thumb_x = screen_width / frame_width * x
                    thumb_y = screen_height / frame_height * y
                    
                    # Calculate distance for clicking
                    if index_y != 0 and abs(index_y - thumb_y) < 30:
                        pyautogui.click()
                        pyautogui.sleep(0.5)
                        
    cv2.imshow('AI Virtual Mouse', frame)
    
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cam.release()
cv2.destroyAllWindows()
