import os 
from PIL import Image

def merge_images(folder_names, output_filename):
    images = []
    for folder_name in folder_names:
        if os.path.isdir(folder_name):
            for filename in os.listdir(folder_name):
                if filename.endswith('.jpg') or filename.endswith('.png') or filename.endswith('.jpeg'):
                    img_path = os.path.join(folder_name, filename)
                    img = Image.open(img_path)
                    images.append(img)
        else:
            print(f"Folder '{folder_name}' does not exist.")

    if images:
        images[0].save(output_filename, save_all=True, append_images=images[1:])
        print(f"Images merged into '{output_filename}' successfully.")
    else:
        print("No images found in the provided folders.")


folder_names = ["1369_12_Наклейки 3-D_3", "1388_6_Наклейки 3-D_2", "1388_2_Наклейки 3-D_1", "1388_12_Наклейки 3-D_3"] # спиок папок
output_filename = 'Result.tif' # готовый tif файл
merge_images(folder_names, output_filename)
