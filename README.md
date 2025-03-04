Image to PDF Converter

Description

This script compresses images and merges them into a single PDF file. It supports various image formats and ensures optimal quality by resizing images while maintaining aspect ratios.

Prerequisites

Before running the script, ensure you have the following installed:

Required Python Libraries:
1. Pillow (for image processing)
2. ReportLab (for PDF generation)
3. pyheif (optional, for handling HEIC format)

Installation Commands:
pip install pillow reportlab
pip install pyheif  (#Only if working with HEIC images)

Supported Image Formats

PNG, JPG, JPEG, GIF, BMP, TIFF, WEBP, HEIC
SVG files are not supported and will be skipped automatically.

How to Use!

1. Prepare the Images
    Place the images inside the directory:
    ~/Downloads/imgToPDF/Images Here
    Ensure that the images are in a supported format.

2. Run the Script
    Open a terminal or command prompt.
    Navigate to the script's location.
    Execute the script using Python:
    python script_name.py
    The script will process the images and generate a merged PDF file.

3. Output
    The resulting PDF file will be saved in the same directory with a name similar to:
    Merge ImageXXXX.pdf  #(XXXX is a random number)

Features
    Automatic Image Compression
    Maintains Aspect Ratio
    Handles HEIC Format (if pyheif is installed)
    Progress Display in Terminal
    Removes Temporary Files After Processing

Notes
    If you encounter an error related to pyheif, ensure it is installed if you plan to process HEIC images.

    The script automatically filters and processes only valid image files in the specified directory.

License
This script is free to use and modify.