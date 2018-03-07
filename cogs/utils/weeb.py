import aiohttp
import urllib
import config


class AppURLopener(urllib.request.FancyURLopener):
    version = "Mozilla/5.0"


async def request_image(type):
    url = f"https://api.weeb.sh/images/random?type={type}&hidden=false"
    async with aiohttp.ClientSession() as session:
        async with session.get(url, headers={"Authorization": config.weeb_token}) as resp:
            j = await resp.json()
            return j['url']


async def request_image_as_gif(type):
    url = f"https://api.weeb.sh/images/random?type={type}&hidden=false&filetype=gif"
    async with aiohttp.ClientSession() as session:
        async with session.get(url, headers={"Authorization": config.weeb_token}) as resp:
            j = await resp.json()
            return j['url']


async def request_image_as_png(type):
    url = f"https://api.weeb.sh/images/random?type={type}&hidden=false&filetype=png"
    async with aiohttp.ClientSession() as session:
        async with session.get(url, headers={"Authorization": config.weeb_token}) as resp:
            j = await resp.json()
            return j['url']


def save_to_image(url, name):
    opener = AppURLopener()
    response = opener.open(url)
    data = response.read()
    with open("./images/" + name, "wb") as img:
        img.write(data)
        img.close()