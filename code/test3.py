import cv2
import mediapipe as mp
import math
import csv
# 初始化 Mediapipe 相關物件
mp_drawing = mp.solutions.drawing_utils
mp_drawing_styles = mp.solutions.drawing_styles
mp_face_mesh = mp.solutions.face_mesh

# 讀取圖片
img = cv2.imread(r"C:\Users\stone\poject\N1\test_0001 (11).jpg")

# 初始化座標變數
data_list = []
# 開始進行臉部特徵點檢測
with mp_face_mesh.FaceMesh(
    max_num_faces=1,
    refine_landmarks=True,
    min_detection_confidence=0.5,
    min_tracking_confidence=0.5
) as face_mesh:
    img = cv2.cvtColor(cv2.flip(img, 1), cv2.COLOR_BGR2RGB)
    results = face_mesh.process(img)
    img = cv2.cvtColor(img, cv2.COLOR_RGB2BGR)
    
    if results.multi_face_landmarks:
        for face_landmarks in results.multi_face_landmarks:
            selected_landmarks = [4,130, 359, 291, 61,383,124]
            for id, lm in enumerate(face_landmarks.landmark): 
                if id in selected_landmarks:
                    ih, iw, ic = img.shape
                    x, y = int(lm.x * iw), int(lm.y * ih)
                    outputdata = {"ID": id, "X": x, "Y": y}
                    p_dict = {}
                    output_dict = {}
                    distance=[]
                    if outputdata not in data_list:
                        data_list.append(outputdata)
                        for id in selected_landmarks:
                            if outputdata["ID"] == id:
                                if id == 4:
                                    p1_x = outputdata["X"]
                                    p1_y = outputdata["Y"]
                                else:
                                    p_dict[id] = (outputdata["X"]-p1_x, outputdata["Y"]-p1_y)
                                    #print("ID=", id, "X:", p_dict[id][0], "Y:", p_dict[id][1])
                                    output_dict[id] = {"X": p_dict[id][0], "Y": p_dict[id][1]}
                                    distance = (f"4 to {id}",math.sqrt((outputdata["X"] - 0)**2 + (outputdata["Y"] - 0)**2))
                                    with open('distancesave.csv', 'a', newline='') as file:
                                        writer = csv.writer(file)
                                        # Write the header
                                        writer.writerow(["Landmarks", "Distance"])
                                        # Write the distance
                                        writer.writerow(distance)

