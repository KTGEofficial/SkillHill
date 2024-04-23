# This script right here is the main reason why I joined GitHub.
# This is a really difficult Python script to make.
# Please fix all the errors in my script.
# Can you also make this script more efficient as well?


import os
import math
from PIL import Image, ImageDraw, ImageFont

image_folder_path = "C:\\Users\\test\\OneDrive\\Desktop\\New Folder\\SkillHill\\AdvancedLeaderboard\\OutputFrames"

fps = 24
placingDuration = 96  # Frames
contestant_count = 19
waitTime = 48  # Frames
datasetScore = [333, 313, 310, 266, 222, 218, 206, 196, 183, 182, 170, 168, 165, 162, 156, 156, 155, 155, 153]
datasetTime = [76, 85, 123, 95, 72, 69, 99, 77, 68, 73, 133, 74, 97, 93, 105, 91, 103, 109, 84]
datasetHealth = [58, 60, 87, 57, 36, 34, 47, 34, 28, 31, 55, 29, 36, 34, 38, 33, 36, 38, 29]
datasetOther = [1, 0, 1, 0, 0, 0, 1, 0, 0, 1, 2, 1, 0, 0, 1, 1, 0, 0, 0]
names = ["Test | TST", "Test | TST", "Test | TST", "Test | TST", "Test | TST", "Test | TST", "Test | TST", "Test | TST", "Test | TST", "Test | TST", "Test | TST", "Test | TST", "Test | TST", "Test | TST", "Test | TST", "Test | TST", "Test | TST", "Test | TST", "Test | TST"]
# What images you use to test it with don't matter. Same for the font. I will upload the font to GitHub if I can. I can't upload the images, because there is too many of them for now.
contestantImages = ["C:\\Users\\test\\OneDrive\\Desktop\\New Folder\\SkillHill\\AdvancedLeaderboard\\ImageFolder\\Ct.png", "C:\\Users\\test\\OneDrive\\Desktop\\New Folder\\SkillHill\\AdvancedLeaderboard\\ImageFolder\\Ct.png", "C:\\Users\\test\\OneDrive\\Desktop\\New Folder\\SkillHill\\AdvancedLeaderboard\\ImageFolder\\Cx.png", "C:\\Users\\test\\OneDrive\\Desktop\\New Folder\\SkillHill\\AdvancedLeaderboard\\ImageFolder\\Tr.png", "C:\\Users\\test\\OneDrive\\Desktop\\New Folder\\SkillHill\\AdvancedLeaderboard\\ImageFolder\\Zy.png", "C:\\Users\\test\\OneDrive\\Desktop\\New Folder\\SkillHill\\AdvancedLeaderboard\\ImageFolder\\Xm.png", "C:\\Users\\test\\OneDrive\\Desktop\\New Folder\\SkillHill\\AdvancedLeaderboard\\ImageFolder\\Cm.png", "C:\\Users\\test\\OneDrive\\Desktop\\New Folder\\SkillHill\\AdvancedLeaderboard\\ImageFolder\\Nn.png", "C:\\Users\\test\\OneDrive\\Desktop\\New Folder\\SkillHill\\AdvancedLeaderboard\\ImageFolder\\Bh.png", "C:\\Users\\test\\OneDrive\\Desktop\\New Folder\\SkillHill\\AdvancedLeaderboard\\ImageFolder\\Bn.png", "C:\\Users\\test\\OneDrive\\Desktop\\New Folder\\SkillHill\\AdvancedLeaderboard\\ImageFolder\\Cs.png", "C:\\Users\\test\\OneDrive\\Desktop\\New Folder\\SkillHill\\AdvancedLeaderboard\\ImageFolder\\Lu.png", "C:\\Users\\test\\OneDrive\\Desktop\\New Folder\\SkillHill\\AdvancedLeaderboard\\ImageFolder\\Vm.png", "C:\\Users\\test\\OneDrive\\Desktop\\New Folder\\SkillHill\\AdvancedLeaderboard\\ImageFolder\\Th.png", "C:\\Users\\test\\OneDrive\\Desktop\\New Folder\\SkillHill\\AdvancedLeaderboard\\ImageFolder\\Mj.png", "C:\\Users\\test\\OneDrive\\Desktop\\New Folder\\SkillHill\\AdvancedLeaderboard\\ImageFolder\\Xa.png", "C:\\Users\\test\\OneDrive\\Desktop\\New Folder\\SkillHill\\AdvancedLeaderboard\\ImageFolder\\Mb.png", "C:\\Users\\test\\OneDrive\\Desktop\\New Folder\\SkillHill\\AdvancedLeaderboard\\ImageFolder\\Zk.png", "C:\\Users\\test\\OneDrive\\Desktop\\New Folder\\SkillHill\\AdvancedLeaderboard\\ImageFolder\\Qb.png"]
min_val = 150
step = 50
max_val = 350
margin = 24
graphWidth = 640
textHeight = 30
x = 0

font_path = "C:\\Users\\test\\OneDrive\\Desktop\\New Folder\\SkillHill\\Typefaces\\PixifyRegular.ttf"
text_size = 50
offset = 25
tagSheet = []

os.makedirs(image_folder_path, exist_ok=True)

image_size = (1920, 1080)
background_color = (0, 0, 0)
image = Image.new("RGB", image_size, background_color)
draw = ImageDraw.Draw(image)
font = ImageFont.truetype(font_path, text_size)

def frame_create(image_folder, font_path, text_size, frame_numero, otherState):
    for i in range(math.floor((max_val - min_val) / step) + 2):
        y = (margin + (1080 - (textHeight + margin))) / (((max_val - min_val) / step)) + 1)
        draw.line([(margin, (1080 - (textHeight + margin)) - (y * i)), (graphWidth, y)], fill="yellow", width=4)
    draw.text((160, (1080 - (textHeight + margin)) - (textHeight + 6), str(min_val), "white", font)
    draw.text((160, (margin + textHeight + 6)), str(max_val), "white", font)
    if otherState == 0:
        y = (((math.exp(-0.08 * (otherState - 86.5)) * math.sin(otherState - 86.5) + datasetScore[len(tagSheet)])) - min_val) / (max_val - min_val)) * (margin - (1080 - (textHeight + margin))) + (1080 - (textHeight + margin))
        draw.rectangle((margin, y - (textHeight + 15), graphWidth, y + (textHeight + 15)), (255, 0, 0))
        draw.text((margin + 15, y), f"{names[len(tagSheet)][-3:]} | {round(math.exp(-0.08 * (x - 86.5)) * math.sin(x - 86.5) + datasetScore[len(tagSheet)])}", "white", font)
    if otherState >= 1:
        y = ((datasetScore[len(tagSheet)] - min_val) / (max_val - min_val)) * (margin - (1080 - margin)) + (1080 - margin)) - (textHeight / 2)
        draw.rectangle((margin, y - textHeight, graphWidth, y + textHeight), (255, 0, 0))
        draw.text((margin + 15, y), f"{names[len(tagSheet)][-3:]} | {round(datasetScore[len(tagSheet)])}", "white", font)
        otherState -= 1
    if frame_numero >= placingDuration + waitTime:
        for i in range((frame_numero + 1) // (placingDuration + waitTime)):
            draw.text((margin + 15, datasetScore[i]), f"{names[i]} | {datasetScore[i]}", "white", font)
    source_image = Image.open(contestantImages[len(tagSheet)])
    x_offset = (1920 - (source_image.width // 2)) // 2
    y_offset = (1080 - (source_image.height // 2)) // 2
    scaled_source_image = source_image.resize((source_image.width // 2, source_image.height // 2))
    image.paste(scaled_source_image, (x_offset, y_offset))
    for i in range(contestant_count - (len(tagSheet) + 1)):
        other_image = Image.open(contestantImages[i])
        x_offset = 1920 - (other_image.width // 16)
        y_offset = (1080 - ((other_image.height // 16) * i))
        scaled_other_image = other_image.resize((other_image.width // 16, other_image.height // 16))
        image.paste(scaled_other_image, (x_offset, y_offset))
    draw.text((0, 1080 - text_size), names[math.floor((frame_numero + 1) // (placingDuration + waitTime))], "white", font)
    frame_filename = f"frame_{frame_numero:04d}.png"
    image.save(os.path.join(image_folder, frame_filename))

for i in range(((placingDuration + waitTime) * contestant_count)):
    if i % (placingDuration + waitTime) == 0:
        tagSheet.append(f"{names[len(tagSheet)][:3]} | {datasetScore[len(tagSheet)]}")
    if (i - (len(tagSheet) * waitTime)) % placingDuration == 0:
        x = waitTime
    frame_create(image_folder_path, font_path, text_size, i, x)

