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

def pars_sender(url):
    response = requests.get(url)
    data = response.json()
    return data["message"]["sender"]


def pars_listener(url):
    response = requests.get(url)
    data = response.json()
    return data["message"]["listener"]


def draw():
    map = generate_map()
    x = np.arange(0, 256, 1)
    y = np.arange(0, 256, 1)
    X, Y = np.meshgrid(x, y)
    Z = map
    API_URL = "https://olimp.miet.ru/ppo_it/api/coords"

    dot_first = pars_listener(API_URL)
    dot_second = pars_sender(API_URL)

    fig = plt.figure(figsize=(10, 8))
    ax = fig.add_subplot(111, projection='3d')

    surf = ax.plot_surface(X, Y, Z, cmap=cm.coolwarm,
                          linewidth=0, antialiased=False)
    pics = find(map)
    # Добавляем зеленые точки для dot_first и dot_second
    ax.scatter(dot_first[0], dot_first[1], 255, color='green', s=200)
    ax.scatter(dot_second[0], dot_second[1], 255, color='green', s=200)
    for x in range(len(pics)):
        ax.scatter(pics[x][0], pics[x][1], pics[x][2], color='yellow', s=50)
    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    ax.set_zlabel('Высота')
    fig.colorbar(surf, shrink=0.5, aspect=5)

    plt.show()

if __name__ == "__main__":
    draw()