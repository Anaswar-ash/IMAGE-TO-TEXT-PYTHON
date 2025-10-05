import sys
import pytesseract
from PIL import Image
from PyQt6.QtWidgets import (
    QApplication, QMainWindow, QWidget, QVBoxLayout, QPushButton,
    QLabel, QTextEdit, QFileDialog, QScrollArea, QMessageBox
)
from PyQt6.QtGui import QPixmap
from PyQt6.QtCore import Qt

# --- Configuration ---
# If Tesseract is not in your system's PATH, uncomment the following line
# and set the path to your Tesseract executable.
# For example, on Windows:
# pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'


class ImageToTextApp(QMainWindow):
    """
    A PyQt6 application for extracting text from images using Tesseract OCR.
    """
    def __init__(self):
        super().__init__()
        self.image_path = None
        self.init_ui()

    def init_ui(self):
        """
        Initializes the user interface of the application.
        """
        self.setWindowTitle("Image-to-Text OCR Extractor")
        self.setGeometry(100, 100, 800, 600)

        # Main widget and layout
        central_widget = QWidget(self)
        self.setCentralWidget(central_widget)
        main_layout = QVBoxLayout(central_widget)

        # --- UI Components ---

        # Button to open an image
        self.btn_open = QPushButton("Open Image", self)
        self.btn_open.setStyleSheet("QPushButton {padding: 10px; background-color: #007BFF; color: white; border-radius: 5px;}"
                                      "QPushButton:hover {background-color: #0056b3;}")
        self.btn_open.clicked.connect(self.open_image)
        main_layout.addWidget(self.btn_open)

        # Scrollable area for the image
        self.scroll_area = QScrollArea(self)
        self.scroll_area.setWidgetResizable(True)
        self.image_label = QLabel("Please open an image file.", self)
        self.image_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.image_label.setStyleSheet("QLabel {border: 2px dashed #aaa; padding: 10px;}")
        self.scroll_area.setWidget(self.image_label)
        main_layout.addWidget(self.scroll_area, 1) # Give more stretch factor to image

        # Button to extract text
        self.btn_extract = QPushButton("Extract Text", self)
        self.btn_extract.setStyleSheet("QPushButton {padding: 10px; background-color: #28a745; color: white; border-radius: 5px;}"
                                       "QPushButton:hover {background-color: #1e7e34;}")
        self.btn_extract.setEnabled(False)  # Disabled until an image is loaded
        self.btn_extract.clicked.connect(self.extract_text)
        main_layout.addWidget(self.btn_extract)

        # Text area for extracted text
        self.text_output = QTextEdit(self)
        self.text_output.setReadOnly(True)
        self.text_output.setPlaceholderText("Extracted text will appear here...")
        self.text_output.setStyleSheet("QTextEdit {border: 1px solid #ccc; border-radius: 5px;}")
        main_layout.addWidget(self.text_output, 1) # And to the text output

    def open_image(self):
        """
        Opens a file dialog to select an image and displays it.
        """
        file_path, _ = QFileDialog.getOpenFileName(
            self,
            "Open Image",
            "",
            "Image Files (*.png *.jpg *.jpeg *.bmp *.tiff)"
        )

        if file_path:
            self.image_path = file_path
            pixmap = QPixmap(self.image_path)
            # Scale pixmap to fit the label while maintaining aspect ratio
            self.image_label.setPixmap(pixmap.scaled(
                self.image_label.size(),
                Qt.AspectRatioMode.KeepAspectRatio,
                Qt.TransformationMode.SmoothTransformation
            ))
            self.btn_extract.setEnabled(True)
            self.text_output.clear()

    def extract_text(self):
        """
        Extracts text from the loaded image using pytesseract.
        """
        if not self.image_path:
            self.show_error_message("No image loaded.")
            return

        self.text_output.setPlainText("Processing, please wait...")
        # Force UI update
        QApplication.processEvents()

        try:
            img = Image.open(self.image_path)
            # Use pytesseract to do OCR on the image
            text = pytesseract.image_to_string(img, lang='eng')
            self.text_output.setPlainText(text.strip() or "No text could be extracted.")
        except FileNotFoundError:
            self.show_error_message(f"Error: Image file not found at {self.image_path}")
        except Exception as e:
            self.show_error_message(f"An unexpected error occurred: {e}\n\n"
                                      "Please ensure the Tesseract-OCR engine is installed correctly "
                                      "and its path is configured if necessary.")

    def show_error_message(self, message):
        """
        Displays an error message in a dialog box.
        """
        msg_box = QMessageBox(self)
        msg_box.setIcon(QMessageBox.Icon.Critical)
        msg_box.setText(message)
        msg_box.setWindowTitle("Error")
        msg_box.exec()


def main():
    """
    Main function to run the application.
    """
    app = QApplication(sys.argv)
    window = ImageToTextApp()
    window.show()
    sys.exit(app.exec())


if __name__ == "__main__":
    main()
