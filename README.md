### README: MNIST Image Extraction and Visualization with Matplotlib

---

This project demonstrates how to extract the first 10 images of each digit (0-9) from the MNIST training set and plot them in a 10x10 grid using `matplotlib.pyplot.subplot`. The MNIST dataset consists of grayscale images of handwritten digits, each with a size of 28x28 pixels. We will visually represent the first 100 images, grouped by their digit, in a 10x10 tile grid.

#### Files included:
- **mnist_visualization.py**: Python script that performs the extraction of the first 10 images of each digit from the MNIST dataset and plots them using Matplotlib.
- **requirements.txt**: Lists the Python packages required for this project.

---

### Steps Performed:

1. **Dataset Loading**:
   The MNIST dataset is loaded using Keras' built-in dataset loader:
   ```python
   from keras.datasets import mnist
   ```
   The data is split into training and testing sets:
   ```python
   (x_train, y_train), (_, _) = mnist.load_data()
   ```
   Here, `x_train` contains the images and `y_train` contains the corresponding labels (digits 0-9).

2. **Image Extraction**:
   The goal is to extract the first 10 images for each digit. We loop through the training set, maintaining a counter for each digit and stopping once 10 images for each digit are collected.

   ```python
   images_per_digit = 10
   extracted_images = []

   for digit in range(10):
       count = 0
       for i in range(len(y_train)):
           if y_train[i] == digit:
               extracted_images.append(x_train[i])
               count += 1
               if count == images_per_digit:
                   break
   ```
   This results in 100 images in total (10 images for each of the 10 digits).

3. **Image Plotting**:
   Using `matplotlib.pyplot`, we plot these 100 images in a 10x10 grid. Each subplot corresponds to one image, and the entire grid is labeled with digit numbers.

   ```python
   import matplotlib.pyplot as plt

   plt.figure(figsize=(10, 10))

   for i in range(100):
       plt.subplot(10, 10, i + 1)
       plt.imshow(extracted_images[i], cmap='gray')
       plt.axis('off')

   plt.tight_layout()
   plt.show()
   ```

4. **Plot Display**:
   The script creates a window displaying the first 100 MNIST images, arranged in a grid, where each row represents the first 10 instances of digits 0 through 9.

---

### How to Run the Code:

1. **Install dependencies**:
   Run the following command to install the required packages:
   ```bash
   pip install -r requirements.txt
   ```

2. **Run the script**:
   Execute the following command to start the image extraction and display:
   ```bash
   python mnist_visualization.py
   ```

3. **Expected Output**:
   The script will open a Matplotlib window displaying a 10x10 grid of images, where each row contains images of the same digit, from 0 to 9.

---

### Requirements:
- Python 3.x
- Keras
- TensorFlow
- Matplotlib
- NumPy

---

This simple visualization helps in understanding the variety of handwritten digit images in the MNIST dataset and can be used as a starting point for more complex image classification tasks.
