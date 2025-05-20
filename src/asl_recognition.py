import cv2
import numpy as np
import mediapipe as mp
import pyttsx3
import time
from tensorflow.keras.models import load_model

engine = pyttsx3.init()
engine.setProperty('rate', 150)

model = load_model('asl_model.h5')
class_names = np.load('class_names.npy', allow_pickle=True)

mp_hands = mp.solutions.hands
hands = mp_hands.Hands(static_image_mode=False, max_num_hands=1, min_detection_confidence=0.5)
mp_drawing = mp.solutions.drawing_utils

cap = cv2.VideoCapture(0)
last_spoken_time = 0
speak_delay = 2  # Seconds between speech outputs

while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        continue
    
    frame = cv2.flip(frame, 1)
    rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    results = hands.process(rgb_frame)
    
    if results.multi_hand_landmarks:
        for hand_landmarks in results.multi_hand_landmarks:
            mp_drawing.draw_landmarks(frame, hand_landmarks, mp_hands.HAND_CONNECTIONS)
            
            landmarks = []
            for landmark in hand_landmarks.landmark:
                landmarks.extend([landmark.x, landmark.y, landmark.z])
            
            prediction = model.predict(np.array([landmarks]))
            predicted_class = np.argmax(prediction)
            confidence = np.max(prediction)
            
            if confidence > 0.8:
                current_time = time.time()
                sign_name = class_names[predicted_class]
                
                cv2.putText(frame, f"{sign_name} ({confidence:.2f})", 
                            (10, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
                
                if current_time - last_spoken_time > speak_delay:
                    engine.say(sign_name)
                    engine.runAndWait()
                    last_spoken_time = current_time
    
    cv2.imshow('ASL Recognition', frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()