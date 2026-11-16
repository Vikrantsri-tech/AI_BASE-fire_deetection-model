
from pathlib import Path
from collections import Counter

label_folder = Path("dataset/train/labels")

counts = Counter()
total_files = 0

for file in label_folder.glob("*.txt"):
    total_files += 1

    with open(file, "r") as f:
        for line in f:
            parts = line.strip().split()

            if parts:
                counts[parts[0]] += 1

print("\nDataset class distribution:")
print("Total label files:", total_files)

for class_id, count in sorted(counts.items()):
    print(f"Class ID {class_id}: {count} objects")
