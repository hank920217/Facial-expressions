import cv2
import mediapipe as mp
import math

mp_drawing = mp.solutions.drawing_utils
mp_face_mesh = mp.solutions.face_mesh

cap = cv2.VideoCapture(0)

# 要顯示的特定臉部關鍵點索引
specific_landmarks = [1,70,52,55,285,282,30,386,374,159,145,187,192,123,203,118,411,352,423,416,347,4,11,17,61,291]

with mp_face_mesh.FaceMesh(
    max_num_faces=1,
    refine_landmarks=True,
    min_detection_confidence=0.5,
    min_tracking_confidence=0.5
) as face_mesh:
    while True:
        success, img = cap.read()
        if not success:
            print("無法讀取攝影機畫面")
            break

        img = cv2.cvtColor(cv2.flip(img, 1), cv2.COLOR_BGR2RGB)
        results = face_mesh.process(img)
        img = cv2.cvtColor(img, cv2.COLOR_RGB2BGR)

        if results.multi_face_landmarks:
            for face_landmarks in results.multi_face_landmarks:
                for id, lm in enumerate(face_landmarks.landmark): 
                    if id in specific_landmarks:
                        ih, iw, ic = img.shape
                        x, y = int(lm.x * iw), int(lm.y * ih)
                        cv2.circle(img, (x, y), 5, (0, 0, 255), -1)
                        cv2.putText(img, f"({x}, {y})", (x, y), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 255), 1)

                cv2.imshow('Face Landmarks', img)

        if cv2.waitKey(5) & 0xFF == 27:
            break

cap.release()
cv2.destroyAllWindows()