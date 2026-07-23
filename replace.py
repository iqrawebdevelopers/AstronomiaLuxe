import re
import os

path = r"d:\AI Trainings\Website Design\Watch Website\index.html"
with open(path, "r", encoding="utf-8") as f:
    content = f.read()

# 1. Replace the giant inline <img src="data:image/webp;base64,..."> with <img src="./video-frames/frame-0001.jpg">
# Let's find the img tag.
content = re.sub(
    r'<img\s+src="data:image/webp;base64,[^"]*"',
    r'<img src="./video-frames/frame-0001.jpg"',
    content
)

# 2. Replace the FRAME_DATA array
# Generate the new array content
frames = []
for i in range(1, 301):
    frames.append(f'  "./video-frames/frame-{i:04d}.jpg"')
frames_str = "var FRAME_DATA = [\n" + ",\n".join(frames) + "\n];"

content = re.sub(
    r'var\s+FRAME_DATA\s*=\s*\[.*?\];',
    frames_str,
    content,
    flags=re.DOTALL
)

with open(path, "w", encoding="utf-8") as f:
    f.write(content)

print("Replacement complete.")
