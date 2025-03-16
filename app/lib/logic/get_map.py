import sys
import requests
import numpy as np

def fetch_tile(url):
    response = requests.get(url)
    data = response.json()
    return data['message']['data']

def generate_map():
    map_array = np.zeros((256, 256), dtype=int)
    API_URL = "https://olimp.miet.ru/ppo_it/api"
    
    for i in range(4):
        for j in range(4):
            tile = fetch_tile(API_URL)
            start_i = i * 64
            start_j = j * 64
            map_array[start_i:start_i+64, start_j:start_j+64] = tile
    
    return map_array

if __name__ == "__main__":
    result = generate_map()
    print(result)