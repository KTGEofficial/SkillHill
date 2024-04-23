import os
import colorsys
from PIL import Image, ImageDraw, ImageFont

# This might be used in EWOW, or at least a modified and fancier version of it. It adds suspense to elimination, or life loss.

image_folder_path = "C:\\Users\\test\\Desktop\\New Folder\\SkillHill\\BarGraph"
fps = 24
duration = 15
bar_count = 10
bar_width = 192
bar_gap = 0
bar_height = 667
dataset = [245, 312, 178, 421, 199, 287, 156, 398, 223, 375]
tags = ["TS0", "TS1", "TS2", "TS3", "TS4", "TS5", "TS6", "TS7", "TS8", "TS9"]
max_value = 421
x_safe_data_requirement = 421
font_path = "C:\\Users\\test\\Desktop\\New Folder\\SkillHill\\Typefaces\\PixifyRegular.ttf"
text_size = 40
tag_offset = [20, 20, 20, 20, 20, 20, 20, 20, 20, 20]

os.makedirs(image_folder_path, exist_ok=True)
image_size = (1920, 1080)
background_color = (0, 0, 0)
image = Image.new("RGB", image_size, background_color)
draw = ImageDraw.Draw(image)
font = ImageFont.truetype(font_path, text_size)

def frame_create(image_folder, font_path, text_size, frame_numero):
    for i in range(bar_count):
        left = i * (bar_width + bar_gap)
        right = left + bar_width
        top = ((-451 / max_value) * (max_value / ((duration * fps) - 1) * frame_numero)) + bar_height
        bottom = bar_height
        bar_color = []
        text_width, text_height = draw.textsize(text, font=font)
        for j in range(3):
            bar_color.append(round(colorsys.hsv_to_rgb(((max_value / ((duration * fps) - 1) * frame_numero)) / (max_value * 3), 1, 1)[j] * 255))
        position = [(left + right + (- text_width)) / 2, bar_height + tag_offset[i]]
        if ((max_value / ((duration * fps) - 1) * frame_numero)) >= dataset[i]:
            top = ((-451 / max_value) * (dataset[i])) + bar_height
            bar_color = [255, 0, 0]
            if dataset[i] >= x_safe_data_requirement:
                bar_color = [0, 255, 0]
        draw.rectangle([left, top, right, bottom], tuple(bar_color))
        draw.text(position, tags[i], "white", font)
    
    frame_filename = "frame_" + str(frame_numero).zfill(4) + ".png"
    image.save(os.path.join(image_folder, frame_filename))

for i in range((duration * fps)):
    frame_create(image_folder_path, font_path, text_size, i)
