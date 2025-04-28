import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import cv2
import mediapipe as mp
import time
from osc.send_gestures import send_gesture
from osc.send_gestures import send_gesture, clear_gestures


mp_hands = mp.solutions.hands
hands = mp_hands.Hands(max_num_hands=1, min_detection_confidence=0.7)
mp_draw = mp.solutions.drawing_utils

cap = cv2.VideoCapture(0)
prev_x = None
prev_y = None
last_gesture_time = time.time()

while cap.isOpened():
    success, frame = cap.read()
    if not success:
        continue

    rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    results = hands.process(rgb)

    if results.multi_hand_landmarks:
        for hand_landmarks in results.multi_hand_landmarks:
            mp_draw.draw_landmarks(frame, hand_landmarks, mp_hands.HAND_CONNECTIONS)

            x = hand_landmarks.landmark[0].x
            y = hand_landmarks.landmark[0].y
            current_time = time.time()

            SWIPE_THRESHOLD = 0.05

            # SWIPE LEFT/RIGHT
            if prev_x is not None:
                delta_x = x - prev_x
                if current_time - last_gesture_time > 0.5:
                    if delta_x < -SWIPE_THRESHOLD:
                        print("Swipe Left")
                        send_gesture("swipe_left")
                        last_gesture_time = current_time
                    elif delta_x > SWIPE_THRESHOLD:
                        print("Swipe Right")
                        send_gesture("swipe_right")
                        last_gesture_time = current_time
            prev_x = x

            # SWIPE UP/DOWN
            if prev_y is not None:
                delta_y = y - prev_y
                if current_time - last_gesture_time > 0.5:
                    if delta_y < -SWIPE_THRESHOLD:
                        print("Swipe Up")
                        send_gesture("swipe_up")
                        last_gesture_time = current_time
                    elif delta_y > SWIPE_THRESHOLD:
                        print("Swipe Down")
                        send_gesture("swipe_down")
                        last_gesture_time = current_time
            prev_y = y


            # ZOOM (Pinch Detection)
            thumb = hand_landmarks.landmark[mp_hands.HandLandmark.THUMB_TIP]
            index = hand_landmarks.landmark[mp_hands.HandLandmark.INDEX_FINGER_TIP]
            distance = ((thumb.x - index.x) ** 2 + (thumb.y - index.y) ** 2) ** 0.5

            # Zoom gesture thresholds
            ZOOM_IN_THRESHOLD = 0.17
            ZOOM_OUT_THRESHOLD = 0.05

            # Zoom (Pinch detection)
            if current_time - last_gesture_time > 1.0:  # make it more deliberate
                if distance < ZOOM_OUT_THRESHOLD:
                    print("Zoom Out")
                    send_gesture("zoom_out")
                    last_gesture_time = current_time
                elif distance > ZOOM_IN_THRESHOLD:
                    print("Zoom In")
                    send_gesture("zoom_in")
                    last_gesture_time = current_time

    cv2.imshow('Hand Tracking', frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()


clear_gestures()
