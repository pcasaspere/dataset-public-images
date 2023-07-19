import os
import datetime
import requests
from PIL import Image


def downloadAndSaveImage(url: str, save_path: str) -> None:
    try:
        response = requests.get(url)
        response.raise_for_status()
        with open(save_path, "wb") as f:
            f.write(response.content)
    except requests.exceptions.RequestException as e:
        print(f"Error en descargar l'imatge: {e}")


def cropImage(file_path: str, crop_size: int = 50) -> None:
    img = Image.open(file_path)

    width, height = img.size

    coordenadas_recorte = (0, 0, width, height - crop_size)

    img.crop(coordenadas_recorte).save(file_path)


if __name__ == "__main__":
    print('Start script')

    images_directory = "images"

    targets = {
        'vic': 'http://www.meteosona.com/static/estacions/images/webcams/VicPlaca.jpg'
    }

    if not os.path.exists(images_directory):
        os.makedirs(images_directory)

    for key in targets:
        target = targets[key]
        extension = target.split('.')[-1]
        images_directory_target = f"{images_directory}/{key}"
        file_name = datetime.datetime.now().strftime("%Y_%m_%d_%H_%M") + "." + extension

        if not os.path.exists(f"{images_directory_target}"):
            os.makedirs(images_directory_target)

        save_path = os.path.join(f"{images_directory_target}", file_name)

        downloadAndSaveImage(targets[key], save_path)
        cropImage(save_path)
