from PIL import Image, ImageDraw
import os

# Define the path to save the image sequence
save_folder = "C:\\Users\\mpyle\\OneDrive\\Desktop\\New Folder\\SkillHill\\Transition"

# This is a transition for the standard leaderboard. I split the transition scripts in two, because I don't know how to combine the scripts together.

# Create the save folder if it doesn't exist
os.makedirs(save_folder, exist_ok=True)

# Define the image size (width, height), object size, and the green screen color
image_size = (1920, 1080)
object_size = (1920, 1080)
green_screen_color = (0, 255, 0)

# Define the final position of the black object
final_position = (0, 540)

# Generate 24 images of the black object in its final position
for frame in range(24):
    # Create a new image with a green screen background
    image = Image.new('RGB', image_size, color=green_screen_color)
    draw = ImageDraw.Draw(image)
    
    # Draw the black object on the image at its final position
    draw.rectangle([final_position, (final_position[0] + object_size[0], final_position[1] + object_size[1])], fill='black')
    
    # Save the image
    image_path = os.path.join(save_folder, f'frame_{(frame + 48):03d}.png')
    image.save(image_path)

print(f"Generated 24 images of the black object in its final position with a green screen background. Saved to {save_folder}")