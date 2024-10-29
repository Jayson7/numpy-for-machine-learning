import numpy as np
from PIL import Image

# Load an image
image = Image.open("images.png")
image_array = np.array(image)

# Function to convert image to grayscale
def to_grayscale(img_array):
    # Calculate weighted average for RGB to grayscale conversion
    grayscale = np.dot(img_array[..., :3], [0.2989, 0.5870, 0.1140])
    return grayscale.astype(np.uint8)

# Apply grayscale conversion
gray_image_array = to_grayscale(image_array)
gray_image = Image.fromarray(gray_image_array)
gray_image.show()

# Function to flip the image horizontally
def flip_horizontal(img_array):
    return np.flip(img_array, axis=1)

# Apply horizontal flip
flipped_horizontal_array = flip_horizontal(image_array)
flipped_horizontal_image = Image.fromarray(flipped_horizontal_array)
flipped_horizontal_image.show()

# Function to flip the image vertically
def flip_vertical(img_array):
    return np.flip(img_array, axis=0)

# Apply vertical flip
flipped_vertical_array = flip_vertical(image_array)
flipped_vertical_image = Image.fromarray(flipped_vertical_array)
flipped_vertical_image.show()

# Function to rotate the image by 90 degrees
def rotate_90(img_array):
    return np.rot90(img_array)

# Apply 90-degree rotation
rotated_array = rotate_90(image_array)
rotated_image = Image.fromarray(rotated_array)
rotated_image.show()

# Function to apply a basic blur effect
def blur_image(img_array, kernel_size=3):
    # Create an empty array for the output
    blurred_array = img_array.copy()
    for i in range(kernel_size // 2, img_array.shape[0] - kernel_size // 2):
        for j in range(kernel_size // 2, img_array.shape[1] - kernel_size // 2):
            # Calculate the average value in the neighborhood
            blurred_array[i, j] = np.mean(
                img_array[i - kernel_size // 2:i + kernel_size // 2 + 1,
                          j - kernel_size // 2:j + kernel_size // 2 + 1],
                axis=(0, 1)
            )
    return blurred_array.astype(np.uint8)

# Apply blur effect
blurred_image_array = blur_image(image_array)
blurred_image = Image.fromarray(blurred_image_array)
blurred_image.show()
