from PIL import Image
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter
import os
import random
import sys

user = input("Please Enter to start...")

# List of supported image formats
SUPPORTED_FORMATS = (".png", ".jpg", ".jpeg", ".gif", ".bmp", ".tiff", ".webp", ".heic")

def compress_images_to_single_pdf(image_paths, output_pdf):
    try:
        temp_images = []  # Store temporary compressed images
        c = canvas.Canvas(output_pdf, pagesize=letter)
        pdf_width, pdf_height = letter
        total_images = len(image_paths)

        for index, img_path in enumerate(image_paths, start=1):
            try:
                ext = os.path.splitext(img_path)[1].lower()

                # Skip unsupported file formats (e.g., SVG)
                if ext == ".svg":
                    print(f"Skipping unsupported format: {img_path}")
                    continue
                
                # Open the image
                img = Image.open(img_path)

                # Convert HEIC to RGB (if pyheif is installed)
                if ext == ".heic":
                    try:
                        import pyheif
                        heif_file = pyheif.read(img_path)
                        img = Image.frombytes(heif_file.mode, heif_file.size, heif_file.data)
                    except ImportError:
                        print(f"Skipping {img_path}: pyheif module not installed")
                        continue

                # Convert to RGB if needed (for consistent output)
                if img.mode != "RGB":
                    img = img.convert("RGB")

                # Resize image while maintaining aspect ratio
                max_size = (1200, 1600)  # Adjust as needed
                img.thumbnail(max_size, Image.LANCZOS)

                # Get image dimensions
                img_width, img_height = img.size
                scale_factor = min(pdf_width / img_width, pdf_height / img_height)
                scaled_width = img_width * scale_factor
                scaled_height = img_height * scale_factor

                # Calculate centered position
                x = (pdf_width - scaled_width) / 2
                y = (pdf_height - scaled_height) / 2

                # Save a temporary compressed image
                temp_path = f"temp_{random.randint(1000, 9999)}.jpg"
                img.save(temp_path, "JPEG", quality=90)
                temp_images.append(temp_path)

                # Draw image onto PDF
                c.drawImage(temp_path, x, y, scaled_width, scaled_height)
                c.showPage()

                # Calculate and print progress percentage
                progress = (index / total_images) * 100
                sys.stdout.write(f"\rProcessing: {progress:.2f}%")
                sys.stdout.flush()

            except Exception as img_error:
                print(f"\nSkipping {img_path}: {img_error}")

        c.save()

        # Remove temporary files
        for temp in temp_images:
            os.remove(temp)

        print(f"\nSuccessfully compressed and merged images into {output_pdf}")
    except Exception as e:
        print(f"Error: {e}")

# Define directory path
home_directory = os.path.expanduser("~")
directory = os.path.join(home_directory, "Downloads", "image-to-pdf-master", "Images Here")

# List all files in the directory
files = os.listdir(directory)

# Define image file extensions
image_extensions = ('.png', '.jpg', '.jpeg', '.gif', '.bmp', '.tiff', '.webp', '.heic', '.svg')

# Filter image files
arrayImage = [file for file in files if file.lower().endswith(image_extensions)]

# Example usage
image_files = [os.path.join(directory, file) for file in arrayImage]

random_number = random.randint(1000, 9999)
output_pdf_file = f"Merge Image{random_number}.pdf"

compress_images_to_single_pdf(image_files, output_pdf_file)
