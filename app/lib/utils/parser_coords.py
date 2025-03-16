import requests

from app.lib.database import addCoords


API_URL = "https://olimp.miet.ru/ppo_it/api/coords"


def pars_sender(url):
    response = requests.get(url)
    data = response.json()
    return data["message"]["listener"]


def pars_listener(url):
    response = requests.get(url)
    data = response.json()
    return data["message"]["price"]


def pars_price(url):
    response = requests.get(url)
    data = response.json()
    return data["message"]["sender"]


def parse_all_and_save(url):
    addCoords(pars_sender(url), pars_listener(url), pars_price(url))


print(pars_sender(API_URL))
print(pars_listener(API_URL))
print(pars_price(API_URL))
