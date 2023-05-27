# Image Filtering App

This is a PyQt-based application that allows users to load an image, apply various filters to it, and save the filtered image. The application provides a user-friendly interface to select different filters and visualize the original and filtered images.

## Features
Load an image from the file system.

Apply filters such as:
grayscale, 
blur, 
edge detection, 
sepia, 
invert colors, 
sharpen, 
emboss, 
brightness, 
contrast, 
custom filter 1, and custom filter 2

View the original and filtered images side by side
Save the filtered image to a file

### Prerequisites
Python 3
PyQt5
OpenCV
NumPy

## Installation
![photo1685198009](https://github.com/neostar08/Python/assets/119280926/3a3db52f-7d9b-4d03-b01b-fb3d8af9a3f2)

The application window will appear, providing the following functionality:

### Load Image: 
Click this button to open a file dialog and select an image file to load.
### Filter: 
Choose a filter from the drop-down list to apply to the loaded image.
### Apply Filter: 
Click this button to apply the selected filter to the original image and display the filtered image.
### Save Image: 
After applying a filter, click this button to save the filtered image to a file.
### Custom Filters
The application includes two custom filters that you can modify to implement your own image processing logic:
Run the app.py file to start the application.
Click on the "Load Image" button to select an image file from your computer.
Choose a filter option from the dropdown menu.
Click on the "Apply Filter" button to apply the selected filter to the image.
The original image and the filtered image will be displayed side by side.



## The following filters are available in the app:

Grayscale: Converts the image to grayscale.
Blur: Applies Gaussian blur to the image.
Edge Detection: Detects edges in the image using the Canny edge detection algorithm.
Sepia: Applies a sepia tone effect to the image.
Invert Colors: Inverts the colors of the image.
Sharpen: Enhances the sharpness of the image.
Emboss: Adds an embossed effect to the image.
Brightness: Adjusts the brightness of the image.
Contrast: Adjusts the contrast of the image.



## Examples


### Here are some examples showcasing the image filtering app in action:

1

![photo1685196455](https://github.com/neostar08/Python/assets/119280926/11b87a3b-4356-4bc6-aae7-a2a9848b1360)

2

![photo1685196572](https://github.com/neostar08/Python/assets/119280926/b2b05cc7-e783-402a-83e5-e34fbc37a2ff)

3

![photo1685196589](https://github.com/neostar08/Python/assets/119280926/643ba130-82d0-4cbe-be95-05952cc0496e)




## License
This project is licensed under the MIT License.

## Acknowledgments
The application was developed using the following technologies and resources:

Python: https://www.python.org/


PyQt5: https://www.riverbankcomputing.com/software/pyqt/


OpenCV: https://opencv.org/


NumPy: https://numpy.org/

## Repository Information

The provided code is a Python script for an "Image Filtering App" that allows users to load images, apply various filters, and save the filtered images. The code utilizes the following libraries:


### PyQt5: 


PyQt5 is a Python binding for the Qt framework. It provides a set of Python modules that enable developers to create desktop applications with a graphical user interface. In this code, PyQt5 is used to create the GUI components, such as labels, buttons, and combo boxes, and handle user interactions.

### OpenCV:

OpenCV (Open Source Computer Vision Library) is a popular open-source library for computer vision and image processing tasks. It provides a wide range of functions and algorithms for image manipulation, including loading, filtering, and saving images. In this code, OpenCV is used for image loading, applying filters, and image conversion.



The code follows a simple structure, creating a main application window and setting up the GUI components. Users can load an image, select a filter from the combo box, apply the chosen filter, and save the resulting filtered image.



To run the code, you need to have Python installed on your system, along with the required libraries (PyQt5 and OpenCV). You can execute the script using a Python 
interpreter or an integrated development environment (IDE) that supports Python.



When using this code for your project, it is recommended to provide the necessary installation instructions for the required libraries in your project's README.md file. Additionally, you should include a description of the functionality of your project, the purpose of the Image Filtering App, and any specific instructions or considerations for users who will be interacting with your application. 

The Image Filtering App is a Python script that utilizes OpenAI's ChatGPT language model to enhance the functionality of image filtering.  By leveraging the power of ChatGPT, the app provides precise image processing capabilities and generates visually appealing results.



Remember to acknowledge and provide proper attribution to the PyQt5 and OpenCV libraries in your project, as per their respective licenses and guidelines.

## Repository Structure

### main.py: 

The main Python script that runs the Image Filtering App.


### README.md: 

This file, providing an overview and instructions for the project.


### LICENSE: 

The license file specifying the permissions and restrictions for using the project.


### images/: 

A directory containing sample images for testing the application.


### screenshots/:

A directory to store screenshots of the application for the README.md file.


### docs/:

A directory to store additional documentation or reference materials related to the project.


