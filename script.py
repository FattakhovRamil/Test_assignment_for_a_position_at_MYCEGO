import os 
from PIL import Image
import argparse
import numpy as np

def merge_images(folder_path, output_filename, margin=10, spacing=10):
    images = []

    for filename in os.listdir(folder_path):
        if filename.endswith('.jpg') or filename.endswith('.png') or filename.endswith('.jpeg'):
            img_path = os.path.join(folder_path, filename)
            img = Image.open(img_path)
            images.append(img)
    
    num_images = len(images)
    num_columns = (num_images + 1) // 2  

   
    image_width, image_height = images[0].size
    total_width = (image_width + spacing) * num_columns + margin * 2
    total_height = (image_height + spacing) * 2 + margin * 2

    
    result_img = Image.new("RGB", (total_width, total_height), color='white')

   
    for i, img in enumerate(images):
        row = i % 2
        col = i // 2
        x = col * (image_width + spacing) + margin
        y = row * (image_height + spacing) + margin
        result_img.paste(img, (x, y))

    
    result_img.save(output_filename)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Merge images into a TIFF file')
    parser.add_argument('folder_path', type=str, help='Path to the folder containing images')
    parser.add_argument('output_filename', type=str, help='Name of the output TIFF file')
    parser.add_argument('--margin', type=int, default=100, help='Margin around the images')
    parser.add_argument('--spacing', type=int, default=40, help='Spacing between images')
    args = parser.parse_args()

    merge_images(args.folder_path, args.output_filename, args.margin, args.spacing)
