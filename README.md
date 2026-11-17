#🔥 AI-Based Fire & Smoke Detection System

An AI-powered Fire and Smoke Detection System built using **Python, YOLOv8, and OpenCV**. The project uses computer vision and deep learning to identify fire and smoke in images and real-time webcam video.

The main objective is to support early identification of potential fire hazards through automated visual detection.

## 🚀 Features

- Real-time fire and smoke detection using a laptop webcam.
- YOLOv8-based custom-trained object detection model.
- Detection of fire and smoke with bounding boxes.
- Confidence scores for detected objects.
- Image-based fire and smoke detection.
- Adjustable confidence threshold.
- Custom dataset training and model evaluation.

## 🛠️ Technologies Used

- Python 3.13.5
- YOLOv8 (Ultralytics)
- OpenCV
- PyTorch
- Computer Vision
- Deep Learning

## 📁 Project Structure

```text
AI-Fire-Smoke-Detection/
│
├── alert/
│
├── dataset/
│   └── data.yaml
│
├── detection/
│   ├── live_detection.py
│   └── test_model.py
│
├── model/
│   └── fire_smoke.pt
│
├── camera_test.py
├── check_dataset.py
├── inspect_classes.py
├── visualize_labels.py
├── train_model.py
├── resume_training.py
├── .gitignore
└── README.md
```

## ⚙️ Installation and Setup

### 1. Clone the repository

```bash
git clone https://github.com/Vikrantsri-tech/AI_BASE-fire_deetection-model.git
```

### 2. Open the project folder

```bash
cd AI_BASE-fire_deetection-model
```

### 3. Create a virtual environment

```bash
py -m venv venv
```

### 4. Activate the environment (Windows)

```powershell
.\venv\Scripts\Activate.ps1
```

### 5. Install required libraries

```bash
python -m pip install ultralytics opencv-python
```

## 📷 Run Live Webcam Detection

Make sure your trained model is available at:

```text
model/fire_smoke.pt
```

Run the following command:

```bash
python detection/live_detection.py
```

The webcam will start detecting fire and smoke in real time.

**Press Q to close the webcam window.**

## 🧠 Model Training

The project uses a custom fire and smoke dataset with YOLOv8.

To train the model:

```bash
python train_model.py
```

Training results and model weights are saved in the `runs/` directory.

## 📊 Model Performance

The initial 20-epoch training evaluation produced the following validation results:

| Metric | Fire | Smoke |
|---|---:|---:|
| Precision | 69% | 58% |
| Recall | 56.4% | 34.2% |
| mAP50 | 63.5% | 37.4% |

These are experimental results. Further training and dataset improvements are needed to improve detection performance.

## 📚 Dataset Information

The project uses the Fire and Smoke dataset from Roboflow Universe.

**Dataset:** Fire-Smoke-YVnRC

**Source:** https://universe.roboflow.com/eco-group/fire-smoke-yvnrc/dataset/1

**License:** CC BY 4.0

The dataset files are not included in this repository. Download the dataset separately and arrange it according to the paths specified in `dataset/data.yaml`.

## 🔮 Future Improvements

- Multiple-camera monitoring.
- Automatic email and emergency alert notifications.
- Web-based monitoring dashboard.
- Improved detection accuracy.
- Reduction of false-positive detections.
- Better smoke detection performance.

## ⚠️ Disclaimer

This project is an educational and experimental AI prototype. It is not a certified fire detection or life-safety system and must not replace certified smoke detectors, fire alarms, or emergency response systems.

## 👨‍💻 Author

**Vikrant Srivastava**

B.Tech – Computer Science and Engineering

GitHub: https://github.com/Vikrantsri-tech

---

⭐ If you find this project interesting, consider giving the repository a star!
