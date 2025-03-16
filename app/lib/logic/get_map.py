from app.lib.utils.parser_map import fetch_tile

def generate_map():
    map = [[]*64]
    print(tile)
    for i in range(16):
        for j in range(16):
            tile = fetch_tile()
            for x in range(64):
                map[i][j].append(*tile[x])
    return map
