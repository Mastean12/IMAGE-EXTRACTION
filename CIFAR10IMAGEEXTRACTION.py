# Import necessary libraries
import numpy as np
import matplotlib.pyplot as plt
from tensorflow.keras.datasets import mnist

# Load the MNIST dataset
(train_images, train_labels), (test_images, test_labels) = mnist.load_data()

# Initialize a list to store the first 10 images of each digit
images_to_plot = []
labels_to_plot = []

# Extract the first 10 images of each digit (0-9)
for digit in range(10):
    count = 0
    for i in range(len(train_labels)):
        if train_labels[i] == digit:
            images_to_plot.append(train_images[i])
            labels_to_plot.append(train_labels[i])
            count += 1
        if count == 10:  # Stop after finding the first 10 images of this digit
            break

# Convert list to numpy array for easier handling
images_to_plot = np.array(images_to_plot)

# Plot the first 100 images in a 10x10 grid
plt.figure(figsize=(10, 10))
for i in range(100):
    plt.subplot(10, 10, i + 1)
    plt.imshow(images_to_plot[i], cmap='gray')
    plt.axis('off')  # Hide axes for clarity

plt.tight_layout()
plt.show()
