# Facial-expressions

這是一個以 MediaPipe Face Mesh 擷取臉部特徵點，並將特徵轉成距離資料供表情分類使用的 Python 專案。資料集中包含四種表情：`happy`、`sad`、`surprised`、`disgusted`，每個類別各 200 張圖片。

## 專案內容

- `data/`：表情圖片資料集，依表情類別分資料夾存放。
- `modle.py`：定義 `FaceMeshDetector`，使用 MediaPipe Face Mesh 擷取指定臉部 landmark，並將距離特徵寫入 CSV。
- `tool2.py`：批次讀取圖片並呼叫 `FaceMeshDetector.detect()` 產生特徵資料。
- `distancesave .csv`：已產生的訓練特徵資料。
- `distancesavetest.csv`：已產生的測試特徵資料。
- `code/main.py`：開啟攝影機，即時標示指定臉部 landmark 座標。
- `code/test1.py`、`code/test3.py`：單張圖片或測試用的 landmark 距離擷取範例。
- `code/math_1.py`、`code/math_2.py`：計算臉部點位距離與角度的實驗程式。
- `RandomForestClassifier.ipynb.url`：指向 Google Colab 隨機森林分類 notebook 的捷徑。

## 資料集

目前資料夾結構如下：

```text
data/
├── disgusted/   200 images
├── happy/       200 images
├── sad/         200 images
└── surprised/   200 images
```

`modle.py` 內的標籤註解如下：

```text
disgusted = 1
happy = 2
surprised = 3
sad = 4
```

## 環境需求

建議使用 Python 3.9 以上版本，並安裝下列套件：

```bash
pip install opencv-python mediapipe pillow scikit-learn pandas numpy
```

如果只要執行特徵擷取，至少需要：

```bash
pip install opencv-python mediapipe pillow
```

## 使用方式

### 1. 擷取圖片特徵

先修改 `tool2.py` 裡的圖片路徑與表情類別，例如：

```python
for i in range(1, 201):
    detector.detect(r"data/sad/sad({}).jpg".format(i))
```

接著執行：

```bash
python tool2.py
```

程式會透過 `modle.py` 擷取臉部 landmark 特徵，並追加寫入 `distancesave .csv`。

### 2. 開啟攝影機測試 landmark

```bash
python code/main.py
```

畫面會標出指定的臉部特徵點與座標。按下 `Esc` 可結束程式。

### 3. 訓練分類模型

專案提供 `RandomForestClassifier.ipynb.url`，可開啟對應的 Google Colab notebook，使用 CSV 特徵資料訓練 Random Forest 分類器。

## 注意事項

- 部分程式仍保留本機絕對路徑，例如 `C:\Users\stone\...`，在其他電腦執行前需要改成目前專案中的相對路徑。
- `distancesave .csv` 檔名中包含空白，讀寫時要留意檔名是否完全一致。
- 現有 Python 檔名 `modle.py` 可能是 `model.py` 的拼字誤植；若要改名，需要同步修改 `tool2.py` 的 import。
- 專案內有部分舊註解出現亂碼，但核心程式邏輯仍可從程式碼判讀。

## 專案目的

本專案主要用於學習與實驗：

- 使用 MediaPipe 偵測臉部 landmark。
- 將臉部點位轉換成可訓練的數值特徵。
- 使用機器學習模型進行情緒/表情分類。
