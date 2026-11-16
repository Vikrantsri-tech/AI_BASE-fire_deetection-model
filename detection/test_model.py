
from ultralytics import YOLO

# Load our trained model
model = YOLO("model/fire_smoke.pt")

print("Model loaded successfully!")

# Display model classes
print("Classes:", model.names)

# Test on the test dataset images
results = model.predict(
    source="dataset/test/images",
    imgsz=416,
    conf=0.25,
    save=True,
    project="runs",
    name="test_predictions",
    exist_ok=True
)

print("Image testing completed!")
print("Check the runs/test_predictions folder.")
