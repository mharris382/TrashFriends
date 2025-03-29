from PIL import Image
import os

# Folder containing the images
folder_path = 'c:/Users/Richard/GitHub/TrashFriends/.art/2d/'

# Load all images in the folder
images = []
for filename in os.listdir(folder_path):
    if filename.endswith(('.png', '.jpg', '.jpeg', '.webp')):
        img_path = os.path.join(folder_path, filename)
        images.append(Image.open(img_path).convert("RGBA"))
        print(f'Found image: {filename}')

# Ensure there are images to process
if not images:
    raise ValueError('No images found in the folder.')

# Start with the first image as the base
base_image = images[0]

# Resize all images to match the size of the base image
base_size = base_image.size
resized_images = [base_image] + [img.resize(base_size, Image.Resampling.LANCZOS) for img in images[1:]]

# Alpha blend all images together
for img in resized_images[1:]:
    base_image = Image.alpha_composite(base_image, img)

# Save the final composite image as a webp
output_path = os.path.join(folder_path, 'composite_output.webp')
base_image.save(output_path, 'WEBP', quality=80)

print(f"Composite image saved at: {output_path}")