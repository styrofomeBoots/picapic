from PIL import Image
import os

# Parameters
image_folder = './pics'
output_gif = 'output.gif'
max_size = (480, 270)  # Resize to a smaller resolution (change as needed)

# Load and process images
image_files = sorted([f for f in os.listdir(image_folder) if f.endswith('.jpg')])
images = []

for file in image_files:
    img = Image.open(os.path.join(image_folder, file)).convert('P', palette=Image.ADAPTIVE)
    img.thumbnail(max_size, Image.LANCZOS)
    images.append(img)

# Save optimized GIF
images[0].save(
    output_gif,
    save_all=True,
    append_images=images[1:],
    duration=200,
    loop=0,
    optimize=True,
)