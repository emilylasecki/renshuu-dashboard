import os
import requests


def download_image(image_url, file_dir):
    response = requests.get(image_url)

    if response.status_code == 200:
        directory = os.path.dirname(file_dir)
        #if not os.path.exists(directory):
          #  os.makedirs(directory)

        with open(file_dir, "wb") as fp:
            fp.write(response.content)
        print("Image downloaded successfully.")
    else:
        print("Failed to download the image. Status code: {response.status_code}")

if __name__ == "__main__":
    image_url = "https://www.renshuu.org/img/adventure/f/nryjgbz_100_20240408.png"
    file_dir = "myKao.png"
    download_image(image_url, file_dir)