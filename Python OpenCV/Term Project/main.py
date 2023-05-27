import cv2
import tkinter as tk

import numpy as np
from PIL import Image, ImageTk
from tkinter import filedialog

# Initialize the Tkinter app
app = tk.Tk()
app.title("Image Filtering App")


# Function to apply the selected filter to the image
def apply_filter():
    selected_filter = filter_var.get()

    if selected_filter == "Grayscale":
        filtered_image = cv2.cvtColor(original_image, cv2.COLOR_BGR2GRAY)
    elif selected_filter == "Blur":
        filtered_image = cv2.GaussianBlur(original_image, (7, 7), 0)
    elif selected_filter == "Edge Detection":
        filtered_image = cv2.Canny(original_image, 100, 200)
    elif selected_filter == "Sepia":
        filtered_image = cv2.cvtColor(original_image, cv2.COLOR_BGR2RGB)
        filtered_image = cv2.transform(filtered_image,
                                       np.matrix([[0.272, 0.534, 0.131], [0.349, 0.686, 0.168], [0.393, 0.769, 0.189]]))
    elif selected_filter == "Invert Colors":
        filtered_image = cv2.bitwise_not(original_image)
    elif selected_filter == "Sharpen":
        kernel = np.array([[0, -1, 0], [-1, 5, -1], [0, -1, 0]], dtype=np.float32)
        filtered_image = cv2.filter2D(original_image, -1, kernel)
    elif selected_filter == "Emboss":
        kernel = np.array([[2, 0, 0], [0, -1, 0], [0, 0, -1]], dtype=np.float32)
        filtered_image = cv2.filter2D(original_image, -1, kernel)
    elif selected_filter == "Brightness":
        brightness = 50
        filtered_image = cv2.convertScaleAbs(original_image, beta=brightness)
    elif selected_filter == "Contrast":
        contrast = 1.5
        filtered_image = cv2.convertScaleAbs(original_image, alpha=contrast)

    # Convert image to PIL format
    filtered_image = Image.fromarray(filtered_image)

    # Resize image to fit the label
    filtered_image = filtered_image.resize((300, 300))

    # Display the filtered image
    filtered_photo = ImageTk.PhotoImage(filtered_image)
    filtered_label.configure(image=filtered_photo)
    filtered_label.image = filtered_photo


# Function to load the image and initialize the app
