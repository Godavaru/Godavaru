import aiohttp
import urllib
import config


class AppURLopener(urllib.request.FancyURLopener):
    version = "Mozilla/5.0"


def save_to_image(url, name):
    opener = AppURLopener()
    response = opener.open(url)
    data = response.read()
    with open("./images/" + name, "wb") as img:
        img.write(data)
        img.close()