import numpy as np
import matplotlib.pyplot as plt

# --- STEP 1: LOAD THE IMAGE ---
# Note: Since I cannot access your local files, I will generate a
# synthetic "checkerboard" image here so you can run this code immediately.
# In real life, you would use: img = plt.imread('your_photo.jpg')

# Creating a 100x100 synthetic image with random colors
img = np.random.randint(0, 255, (100, 100, 3), dtype=np.uint8)

print(f"Image Shape: {img.shape}")
# Output example: (100, 100, 3) -> (Height, Width, RGB Channels)

# --- STEP 2: TURN IT SPECIFIC COLORS ---
# Let's apply a "Red Filter" by setting Green (index 1) and Blue (index 2) to zero.
red_filtered_img = img.copy() # Always copy to avoid changing the original
red_filtered_img[:, :, 1] = 0 # Zero out Green
red_filtered_img[:, :, 2] = 0 # Zero out Blue

# --- STEP 3: CROP USING SLICING ---
# Syntax: image[ y_start:y_end, x_start:x_end ]
# Let's crop the center 50x50 pixels
center_y, center_x = img.shape[0]//2, img.shape[1]//2
start_y, end_y = center_y - 25, center_y + 25
start_x, end_x = center_x - 25, center_x + 25

cropped_img = img[start_y:end_y, start_x:end_x]

# --- VISUALIZATION ---
plt.figure(figsize=(10, 4))

# Show Original
plt.subplot(1, 3, 1)
plt.title("Original")
plt.imshow(img)
plt.axis('off')

# Show Red Filter
plt.subplot(1, 3, 2)
plt.title("Red Channel Only")
plt.imshow(red_filtered_img)
plt.axis('off')

# Show Crop
plt.subplot(1, 3, 3)
plt.title("Center Crop")
plt.imshow(cropped_img)
plt.axis('off')

plt.tight_layout()
plt.show()