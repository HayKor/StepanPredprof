import sys
import requests
from random import random


API_URL = "https://olimp.miet.ru/ppo_it/api/coords"

def pars_sender(url):
    response = requests.get(url)
    data = response.json()
    return data['message']['listener']

def pars_listener(url):
    response = requests.get(url)
    data = response.json()
    return data['message']['price']

def pars_price(url):
    response = requests.get(url)
    data = response.json()
    return data['message']['sender']

print(pars_sender(API_URL))
print(pars_listener(API_URL))
print(pars_price(API_URL))