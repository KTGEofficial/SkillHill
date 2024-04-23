from PIL import Image, ImageDraw
import os

# Define the path to save the image sequence
save_folder = "C:\\Users\\test\\Desktop\\New Folder\\SkillHill\\Transition"

# This is a transition for the standard leaderboard. I split the transition scripts in two, because I don't know how to combine the scripts together.

# Create the save folder if it doesn't exist
os.makedirs(save_folder, exist_ok=True)

# Define the image size (width, height), object size, and the green screen color
image_size = (1920, 1080)
object_size = (1920, 1080)
green_screen_color = (0, 255, 0)

# Define the number of frames, fps, and the duration of the fall
num_frames = 48  # 24 fps * 2 seconds
fps = 24
fall_duration = 2  # seconds
fall_distance = 540 # pixels (originally 521)

# Calculate the distance the object falls per frame
fall_per_frame = fall_distance / num_frames

# Generate the image sequence
for frame in range(num_frames):
    # Create a new image with a green screen background
    image = Image.new('RGB', image_size, color=green_screen_color)
    draw = ImageDraw.Draw(image)
    
    # Calculate the top left position of the black object for the current frame
    top_left_position = (0, int(fall_per_frame * frame))
    
    # Draw the black object on the image
    draw.rectangle([top_left_position, (top_left_position[0] + object_size[0], top_left_position[1] + object_size[1])], fill='black')
    
    # Save the image
    image_path = os.path.join(save_folder, f'frame_{frame:03d}.png')
    image.save(image_path)

print(f"Generated a 24 fps image sequence of a black object falling down with a green screen background. Saved to {save_folder}")