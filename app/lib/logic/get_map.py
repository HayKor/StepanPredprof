import numpy as np
import requests

from ..database import *


def fetch_tile(url: str):
    response = requests.get(url)
    data = response.json()
    return data["message"]["data"]


def generate_map(url: str):
    map_array = np.zeros((256, 256), dtype=int)

    for i in range(4):
        for j in range(4):
            tile = fetch_tile(url)
            start_i = i * 64
            start_j = j * 64
            map_array[start_i : start_i + 64, start_j : start_j + 64] = tile
    # Сохраняем в базу данных
    addMatrix(map_array)
    return map_array


if __name__ == "__main__":
    API_URL = "https://olimp.miet.ru/ppo_it/api"
    result = generate_map(API_URL)
    print(result)

