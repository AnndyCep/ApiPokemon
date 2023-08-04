from rembg import remove
from PIL import Image
import sys
import os

def main():
    input_path = 'fotos/'
    output_path = 'sinfondo/'

    # Obtener una lista de todas las imágenes en la carpeta input_path
    images = os.listdir(input_path)

    # Iterar sobre cada imagen y procesarla
    for image in images:
        input_file_path = os.path.join(input_path, image)
        output_file_path = os.path.join(output_path, image)

        # Abrir la imagen y procesarla con rembg
        input_image = Image.open(input_file_path)
        output_image = remove(input_image)

        # Guardar la imagen sin fondo en la carpeta de salida
        output_image.save(output_file_path)

if __name__ == '__main__':
    main()


