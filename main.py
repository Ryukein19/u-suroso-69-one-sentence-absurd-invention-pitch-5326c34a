import os
# One-liner entry (220 chars max): the line below is the entire submission.
# Writes the line to /output/entry.txt.
LINE = "A fridge light that dims politely when you open the door at 2 a.m., so it stops judging you for the midnight snack it already knows about."
os.makedirs("/output", exist_ok=True)
open("/output/entry.txt", "w", encoding="utf-8").write(LINE)
