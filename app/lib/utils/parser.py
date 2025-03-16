import sys
import requests
import numpy as np
from random import random


API_URL = "https://olimp.miet.ru/ppo_it/api"

def fetch_tile(url):
    response = requests.get(url)
    data = response.json()
    return data['message']['data']

