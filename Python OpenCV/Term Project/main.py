import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QVBoxLayout, QWidget, QComboBox, QPushButton, \
    QFileDialog
from PyQt5.QtGui import QPixmap, QImage, QFont, QPalette, QColor
from PyQt5.QtCore import Qt
import cv2
import numpy as np


class ImageFilteringApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Image Filtering App")
        self.setGeometry(100, 100, 1400, 1000)

        # Create a central widget and a layout for it
        central_widget = QWidget(self)
        self.setCentralWidget(central_widget)
        layout = QVBoxLayout(central_widget)

        # Create a label for displaying the original image
        self.original_label = QLabel(self)
        layout.addWidget(self.original_label)

        # Create a combo box for selecting the filter
        self.filter_combo = QComboBox(self)
        self.filter_combo.addItem("Grayscale")
        self.filter_combo.addItem("Blur")
        self.filter_combo.addItem("Edge Detection")
        self.filter_combo.addItem("Sepia")
        self.filter_combo.addItem("Invert Colors")
        self.filter_combo.addItem("Sharpen")
        self.filter_combo.addItem("Emboss")
        self.filter_combo.addItem("Brightness")
        self.filter_combo.addItem("Contrast")
        self.filter_combo.addItem("Custom Filter 1")
        self.filter_combo.addItem("Custom Filter 2")
        layout.addWidget(self.filter_combo)

        # Create a button for loading the image
        load_button = QPushButton("Load Image", self)
        load_button.clicked.connect(self.load_image)
        layout.addWidget(load_button)

        # Create a button for applying the filter
        apply_button = QPushButton("Apply Filter", self)
        apply_button.clicked.connect(self.apply_filter)
        layout.addWidget(apply_button)

        # Create a button for saving the filtered image
        save_button = QPushButton("Save Image", self)
        save_button.clicked.connect(self.save_image)
        layout.addWidget(save_button)

        # Create a label for displaying the filtered image
        self.filtered_label = QLabel(self)
        layout.addWidget(self.filtered_label)

        # Set the layout to the central widget
        central_widget.setLayout(layout)

        # Set the background color
        palette = QPalette()
        palette.setColor(QPalette.Background, QColor(165, 171, 194))
        central_widget.setAutoFillBackground(True)
        central_widget.setPalette(palette)

        # Set the style for the filter button
        filter_button_style = """
            QPushButton {
                background-color: rgb(68, 114, 196);
                color: white;
                font-size: 16px;
                font-weight: bold;
                border: none;
                padding: 10px;
            }
            QPushButton:hover {
                background-color: rgb(0, 92, 160);
            }
        """
        apply_button.setStyleSheet(filter_button_style)

        # Initialize variables
        self.original_image = None
        self.filtered_image = None

    def load_image(self):
        file_dialog = QFileDialog(self)
        file_dialog.setFileMode(QFileDialog.ExistingFile)
        file_dialog.setNameFilter("Images (*.png *.xpm *.jpg *.bmp)")
        if file_dialog.exec_():
            file_path = file_dialog.selectedFiles()[0]
            image = QImage(file_path)
            self.original_image = cv2.imread(file_path)
            self.original_image = cv2.cvtColor(self.original_image, cv2.COLOR_BGR2RGB)
            pixmap = QPixmap.fromImage(image)

            # Resize the image to fit the label's dimensions
            label_width = self.original_label.width()
            label_height = self.original_label.height()
            pixmap = pixmap.scaled(label_width, label_height, Qt.KeepAspectRatio)

            self.original_label.setPixmap(pixmap)

    def custom_filter1(self, image):
        # Apply your custom filter 1 logic here
        filtered_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        return filtered_image

    def custom_filter2(self, image):
        # Apply your custom filter 2 logic here
        kernel = np.array([[0, -1, 0],
                           [-1, 5, -1],
                           [0, -1, 0]])
        filtered_image = cv2.filter2D(image, -1, kernel)
        return filtered_image

    def apply_filter(self):
        if self.original_image is None:
            return

        selected_filter = self.filter_combo.currentText()
        self.filtered_image = None

        if selected_filter == "Grayscale":
            self.filtered_image = cv2.cvtColor(self.original_image, cv2.COLOR_BGR2GRAY)
        elif selected_filter == "Blur":
            self.filtered_image = cv2.GaussianBlur(self.original_image, (7, 7), 0)
        elif selected_filter == "Edge Detection":
            gray_image = cv2.cvtColor(self.original_image, cv2.COLOR_BGR2GRAY)
            self.filtered_image = cv2.Canny(gray_image, 100, 200)
        elif selected_filter == "Sepia":
            sepia_kernel = np.array([[0.272, 0.534, 0.131],
                                     [0.349, 0.686, 0.168],
                                     [0.393, 0.769, 0.189]])
            self.filtered_image = cv2.filter2D(self.original_image, -1, sepia_kernel)
        elif selected_filter == "Invert Colors":
            self.filtered_image = 255 - self.original_image
        elif selected_filter == "Sharpen":
            sharpen_kernel = np.array([[0, -1, 0],
                                       [-1, 5, -1],
                                       [0, -1, 0]])
            self.filtered_image = cv2.filter2D(self.original_image, -1, sharpen_kernel)
        elif selected_filter == "Emboss":
            emboss_kernel = np.array([[-2, -1, 0],
                                      [-1, 1, 1],
                                      [0, 1, 2]])
            self.filtered_image = cv2.filter2D(self.original_image, -1, emboss_kernel)
        elif selected_filter == "Brightness":
            brightness = 50
            self.filtered_image = cv2.convertScaleAbs(self.original_image, beta=brightness)
        elif selected_filter == "Contrast":
            contrast = 1.5
            self.filtered_image = cv2.convertScaleAbs(self.original_image, alpha=contrast)
        elif selected_filter == "Custom Filter 1":
            self.filtered_image = self.custom_filter1(self.original_image.copy())
        elif selected_filter == "Custom Filter 2":
            self.filtered_image = self.custom_filter2(self.original_image.copy())

        if self.filtered_image is not None:
            self.filtered_image = cv2.cvtColor(self.filtered_image, cv2.COLOR_BGR2RGB)
            height, width, channel = self.filtered_image.shape
            bytes_per_line = 3 * width

            # Create QImage from filtered image data
            image = QImage(self.filtered_image.data, width, height, bytes_per_line, QImage.Format_RGB888)
            pixmap = QPixmap.fromImage(image)

            # Resize the pixmap to fit the label's dimensions
            label_width = self.filtered_label.width()
            label_height = self.filtered_label.height()
            pixmap = pixmap.scaled(label_width, label_height, Qt.KeepAspectRatio)

            self.filtered_label.setPixmap(pixmap)

    def save_image(self):
        if self.filtered_image is None:
            return

        file_dialog = QFileDialog(self)
        file_dialog.setAcceptMode(QFileDialog.AcceptSave)
        file_dialog.setNameFilter("Images (*.png *.xpm *.jpg *.bmp)")
        if file_dialog.exec_():
            file_path = file_dialog.selectedFiles()[0]
            cv2.imwrite(file_path, self.filtered_image)

            print("Image saved successfully!")


if __name__ == '__main__':
    app = QApplication(sys.argv)
    filtering_app = ImageFilteringApp()
    filtering_app.show()
    sys.exit(app.exec_())
