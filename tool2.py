from modle import FaceMeshDetector

# 建立一個 FaceMeshDetector 物件
detector = FaceMeshDetector()

# 使用 detect 方法來處理一張圖片
for i in  range(1, 201):
    detector.detect(r"C:\Users\stone\MediaPipe\data\sad\sad({}).jpg".format(i))



