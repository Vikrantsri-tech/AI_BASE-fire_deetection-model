
import cv2
from pathlib import Path

image_folder = Path("dataset/train/images")
label_folder = Path("dataset/train/labels")

for label_file in label_folder.glob("*.txt"):

    image_file = image_folder / (label_file.stem + ".jpg")

    if not image_file.exists():
        continue

    image = cv2.imread(str(image_file))

    if image is None:
        continue

    h, w = image.shape[:2]

    with open(label_file, "r") as f:
        for line in f:
            parts = line.split()

            if len(parts) != 5:
                continue

            class_id = int(parts[0])
            x, y, bw, bh = map(float, parts[1:])

            x1 = int((x - bw / 2) * w)
            y1 = int((y - bh / 2) * h)
            x2 = int((x + bw / 2) * w)
            y2 = int((y + bh / 2) * h)

            name = "SMOKE" if class_id == 0 else "FIRE"

            cv2.rectangle(
                image, (x1, y1), (x2, y2),
                (0, 255, 0), 2
            )

            cv2.putText(
                image, name, (x1, max(y1 - 10, 20)),
                cv2.FONT_HERSHEY_SIMPLEX,
                0.6, (0, 255, 0), 2
            )

    cv2.imshow("Dataset Annotation Check", image)

    key = cv2.waitKey(0)

    if key == ord("q"):
        break

cv2.destroyAllWindows()
