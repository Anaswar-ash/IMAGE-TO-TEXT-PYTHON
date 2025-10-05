# Image to Text (OCR)

This Python script extracts text from an image using Tesseract OCR.

## Prerequisites

1.  **Python 3**: Make sure you have Python 3 installed.
2.  **Tesseract OCR Engine**: This script is a wrapper for Google's Tesseract OCR Engine. You need to install it on your system.

    *   **Windows**: Download and run the installer from [Tesseract at UB Mannheim](https://github.com/UB-Mannheim/tesseract/wiki). Make sure to note the installation path. You will likely need to add the Tesseract installation directory to your system's `PATH` environment variable during installation so that the `tesseract` command is available from the command line. A common installation path is `C:\Program Files\Tesseract-OCR`.

    *   **macOS**: You can install it using Homebrew:
        ```bash
        brew install tesseract
        ```

    *   **Linux (Debian/Ubuntu)**:
        ```bash
        sudo apt-get update
        sudo apt-get install tesseract-ocr
        ```

## Setup

1.  **Clone the repository (or download the files).**

2.  **Create a virtual environment (recommended):**
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
    ```

3.  **Install the required Python libraries:**
    ```bash
    pip install -r requirements.txt
    ```

## Usage

Run the script from your terminal and provide the path to the image file as an argument:

```bash
python main.py path/to/your/image.png
```

The script will print the extracted text to the console.

## Example

If you have an image named `sample.png`, you would run:

```bash
python main.py sample.png
```
