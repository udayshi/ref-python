import cv2
import mediapipe as mp
import subprocess
import time
# Initialize MediaPipe Hands model
mp_hands = mp.solutions.hands
hands = mp_hands.Hands(max_num_hands=1, min_detection_confidence=0.7)
mp_drawing = mp.solutions.drawing_utils

# Function to count fingers
def count_fingers(landmarks):
  
    if len(landmarks) != 21:
        return 0
    
    # Get tip positions of fingers (index 4 and 8 for index, 12 and 16 for middle, 20 and 24 for ring and pinky)
    tips = [landmarks[mp_hands.HandLandmark.INDEX_FINGER_TIP],
            landmarks[mp_hands.HandLandmark.MIDDLE_FINGER_TIP],
            landmarks[mp_hands.HandLandmark.RING_FINGER_TIP],
            landmarks[mp_hands.HandLandmark.PINKY_TIP]]
    
    # Get the base positions (index 3 and 7 for index, 11 and 15 for middle, 19 and 23 for ring and pinky)
    bases = [landmarks[mp_hands.HandLandmark.INDEX_FINGER_PIP],
            landmarks[mp_hands.HandLandmark.MIDDLE_FINGER_PIP],
            landmarks[mp_hands.HandLandmark.RING_FINGER_PIP],
            landmarks[mp_hands.HandLandmark.PINKY_PIP]]
    
    fingers = 0
    for tip, base in zip(tips, bases):
        if tip.y < base.y:
            fingers += 1
    
    # Add thumb count (tip is index 4 and base is index 2)
    thumb_tip = landmarks[mp_hands.HandLandmark.THUMB_TIP]
    thumb_base = landmarks[mp_hands.HandLandmark.THUMB_CMC]
    
    if thumb_tip.x > thumb_base.x:
        tdiff=thumb_tip.x-thumb_base.x
        if tdiff > 0.06:
            fingers += 1
        
  
            
    
    return fingers

# Open the camera
cap = cv2.VideoCapture(0)
last_count=0
while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        print("Failed to grab frame")
        break
    
    # Convert the image from BGR to RGB
    rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    
    # Process the RGB frame with MediaPipe Hands
    results = hands.process(rgb_frame)
    
    # Convert the RGB frame back to BGR for display
    frame = cv2.cvtColor(rgb_frame, cv2.COLOR_RGB2BGR)
    
    if results.multi_hand_landmarks:
        for hand_landmarks in results.multi_hand_landmarks:
            mp_drawing.draw_landmarks(frame, hand_landmarks, 
mp_hands.HAND_CONNECTIONS)
            
            # Count fingers
            finger_count = count_fingers(hand_landmarks.landmark)
            cv2.putText(frame, f"Fingers: {finger_count}", (10, 30), 
cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
            if finger_count > last_count or finger_count < last_count:
                last_count=finger_count
               
                

    # Display the resulting frame
    cv2.imshow('Hand Detection', frame)
    
    # Break the loop when 'q' is pressed
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the camera and close all OpenCV windows
cap.release()
cv2.destroyAllWindows()
