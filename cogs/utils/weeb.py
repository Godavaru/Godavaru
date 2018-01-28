import requests
import urllib
import config


class AppURLopener(urllib.request.FancyURLopener):
    version = "Mozilla/5.0"


def request_image(type):
    url = f"https://api.weeb.sh/images/random?type={type}&hidden=false"
    r = requests.get(url,
                     headers={"Authorization": config.weeb_token})
    j = r.json()
    return j['url']


def request_image_as_gif(type):
    url = f"https://api.weeb.sh/images/random?type={type}&hidden=false&filetype=gif"
    r = requests.get(url,
                     headers={"Authorization": config.weeb_token})
    j = r.json()
    return j['url']


def request_image_as_png(type):
    url = f"https://api.weeb.sh/images/random?type={type}&hidden=false&filetype=png"
    r = requests.get(url,
                     headers={"Authorization": config.weeb_token})
    j = r.json()
    return j['url']


def save_to_image(url, name):
    opener = AppURLopener()
    response = opener.open(url)
    data = response.read()
    with open("./images/" + name, "wb") as img:
        img.write(data)
        img.close()