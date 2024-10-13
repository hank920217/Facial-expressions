import cv2
import mediapipe as mp
import math
import csv

class FaceMeshDetector:
    def __init__(self):
        self.mp_drawing = mp.solutions.drawing_utils
        self.mp_drawing_styles = mp.solutions.drawing_styles
        self.mp_face_mesh = mp.solutions.face_mesh
        self.selected_landmarks = [4,130, 359, 291, 61,383,124]

    def detect(self, img_path):
        img = cv2.imread(img_path)
        data_list = []
        distance_list = []  # 新增一個列表來儲存所有的距離
        with self.mp_face_mesh.FaceMesh(
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
                    for id, lm in enumerate(face_landmarks.landmark): 
                        if id in self.selected_landmarks:
                            ih, iw, ic = img.shape
                            x, y = int(lm.x * iw), int(lm.y * ih)
                            outputdata = {"ID": id, "X": x, "Y": y}
                            p_dict = {}
                            distance=[]
                            output_dict = {}
                            if outputdata not in data_list:
                                data_list.append(outputdata)
                                for id in self.selected_landmarks:
                                    if outputdata["ID"] == id:
                                        if id == 4:
                                            p1_x = outputdata["X"]
                                            p1_y = outputdata["Y"]
                                        else:
                                            p_dict[id] = (outputdata["X"]-p1_x, outputdata["Y"]-p1_y)
                                            output_dict[id] = {"X": p_dict[id][0], "Y": p_dict[id][1]}
                                            distance = int(math.sqrt((outputdata["X"] - 0)**2 + (outputdata["Y"] - 0)**2))
                                            distance_list.append(distance)  # 將距離加入列表
        # 在所有距離都蒐集完畢後再寫入CSV檔
        with open('N1test.csv', 'a', newline='') as file:
            writer = csv.writer(file, lineterminator='\n')  # Add lineterminator='\n' to remove blank lines
            writer.writerow(distance_list)

