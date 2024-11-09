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
    image_url = "https://www.renshuu.org/img/adventure/f/acd4vs2_150_20240408.png?v=2"
    file_dir = "myKao2.png"
    download_image(image_url, file_dir)