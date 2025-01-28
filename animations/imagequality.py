import os
from PIL import Image

def reduce_quality(input_folder, output_folder, quality=20):
    # Ensure output directory exists
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    # Iterate through all files in the input directory
    for filename in os.listdir(input_folder):
        if filename.lower().endswith(('.png', '.jpg', '.jpeg', '.tiff', '.bmp', '.gif')):
            # Construct the full file path
            input_path = os.path.join(input_folder, filename)
            output_path = os.path.join(output_folder, filename)

            try:
                # Open and reduce quality
                with Image.open(input_path) as img:
                    # Convert to RGB to avoid issues with saving as JPEG
                    if img.mode in ("RGBA", "P"):
                        img = img.convert("RGB")
                    img.save(output_path, 'JPEG', quality=quality)
                print(f"Processed {filename}")
            except Exception as e:
                print(f"Error processing {filename}: {e}")

# Example usage
input_folder = '/Users/vishnu/Desktop/MusicDanceProject/animations/listening'  # Replace with your input folder path
output_folder = '/Users/vishnu/Desktop/MusicDanceProject/animations/newlistening'  # Replace with your desired output folder path
reduce_quality(input_folder, output_folder, quality=20)  # Adjust quality as needed
