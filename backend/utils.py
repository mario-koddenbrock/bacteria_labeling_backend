import requests
from PIL import Image
from io import BytesIO

def download_image(image_url):
    response = requests.get(image_url)
    img = Image.open(BytesIO(response.content))
    return img
