
from ultralytics import YOLO

print("Loading previous training checkpoint...")

model = YOLO(
    "runs/detect/runs/fire_smoke/weights/last.pt"
)

print("Resuming training from saved progress...")

model.train(resume=True)

print("Training completed!")
