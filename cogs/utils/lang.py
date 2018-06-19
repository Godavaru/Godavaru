import json
import os

BASE_PATH = '../assets/langs/'

langs = dict()
for file in os.listdir(BASE_PATH):
    with open(BASE_PATH + file) as f:
        langs[file] = json.load(f)


def get_lang_string(language: str, json_path: str) -> str:
    lang = langs[language]
    json_list = json_path.split('.')
    for v in json_list:
        lang = lang[v]
    return lang
