import time
from typing import NamedTuple

INPUT_FILE = 'day-9 input.txt'

start_wall_time = time.time()
start_cpu_time = time.process_time()

class Tile(NamedTuple):
    x: int
    y: int

with open(INPUT_FILE) as f:
    content = f.read()

def make_tile(xy: str) -> Tile:
    x, y = map(int, xy.split(","))
    return Tile(x, y)

tiles = [ make_tile(xy) for xy in content.splitlines()]

areas: list[int] = []

for idx, tile1 in enumerate(tiles[:-1], 1):
    for tile2 in tiles[idx:]:
        areas.append((abs(tile2.x - tile1.x)+1) * (abs(tile2.y - tile1.y)+1))

print(max(areas))

elapsed_wall_time = time.time() - start_wall_time
elapsed_cpu_time = time.process_time() - start_cpu_time
print(f"took {elapsed_wall_time:.3f} seconds / {elapsed_cpu_time:.3f} cpu seconds")