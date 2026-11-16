
from pathlib import Path

folder = Path("dataset/train/labels")
count = 0

for file in folder.glob("*.txt"):
    with open(file, "r") as f:
        for line in f:
            parts = line.strip().split()

            if parts and parts[0] == "1":
                print(file.name)
                count += 1
                break

    if count == 5:
        break
