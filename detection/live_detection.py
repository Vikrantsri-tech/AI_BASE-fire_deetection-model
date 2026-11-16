
import cv2
from ultralytics import YOLO

# Load trained model
model = YOLO("model/fire_smoke.pt")

# Open laptop webcam
cap = cv2.VideoCapture(0)

if not cap.isOpened():
    print("Error: Webcam not found!")
    exit()

print("Fire and Smoke Detection Started!")
print("Press Q to stop.")

while True:

    ret, frame = cap.read()

    if not ret:
        print("Cannot read webcam!")
        break

    # Run AI detection
    results = model.predict(
        frame,
        imgsz=416,
        conf=0.40,
        verbose=False
    )

    # Draw detection boxes
    output = results[0].plot()

    # Display video
    cv2.imshow("Fire & Smoke Detection", output)

    # Press Q to exit
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
