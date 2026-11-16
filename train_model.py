
from ultralytics import YOLO
import torch
from pathlib import Path
import shutil

def main():

    print("Using CPU for training")

    # Load pretrained YOLO model
    model = YOLO("yolov8n.pt")

    print("Starting Fire and Smoke Detection training...")

   
results = model.train(
    data="dataset/data.yaml",
    epochs=10,
    imgsz=416,
    batch=2,
    device="cpu",
    workers=0,
    project="runs",
    name="fire_smoke_10",
    exist_ok=True
)


   best_model = Path(
    "runs/detect/runs/fire_smoke_10/weights/best.pt"
)
    if best_model.exists():
        Path("model").mkdir(exist_ok=True)
        shutil.copy2(best_model, "model/fire_smoke.pt")

        print("Training completed successfully!")
        print("Model saved in model/fire_smoke.pt")

if __name__ == "__main__":
    main()
