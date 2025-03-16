import sys
import requests
import numpy as np
import matplotlib.pyplot as plt
import numpy as np
from mpl_toolkits.mplot3d import axes3d


from matplotlib import cm
from matplotlib.ticker import LinearLocator

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

def find(map):
    res = []
    for i in range(1, len(map)-1):
        for j in range(1, len(map[i])-1):
            if map[i + 1][j] < map[i][j] and map[i - 1][j] < map[i][j] and map[i][j+1] < map[i][j] and \
            map[i][j-1] < map[i][j] and map[i+1][j+1] < map[i][j] and map[i+1][j-1] < map[i][j] \
            and map[i-1][j+1] and map[i-1][j-1] < map[i][j]:
                res.append((j, i, int(map[i][j])))
    return res

if __name__ == "__main__":
    map = generate_map()
    x = np.arange(0, 256, 1)
    y = np.arange(0, 256, 1)
    X, Y = np.meshgrid(x, y)
    Z = map

    fig = plt.figure(figsize=(10, 8))
    ax = fig.add_subplot(111, projection='3d')

    surf = ax.plot_surface(X, Y, Z, cmap=cm.coolwarm,
                          linewidth=0, antialiased=False)
    
    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    ax.set_zlabel('Высота')
    fig.colorbar(surf, shrink=0.5, aspect=5)

    plt.show()
