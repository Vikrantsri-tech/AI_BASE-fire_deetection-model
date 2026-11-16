
import cv2

# Open laptop webcam
cap = cv2.VideoCapture(0)

if not cap.isOpened():
    print("Error: Camera not detected!")
    exit()

print("Camera started successfully!")

while True:
    ret, frame = cap.read()

    if not ret:
        print("Unable to capture video")
        break

    cv2.imshow("Fire Detection - Camera Test", frame)

    # Press Q to close camera
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
