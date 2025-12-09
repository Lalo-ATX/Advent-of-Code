import time
from shapely.geometry import Polygon, Point

INPUT_FILE = 'day-9 input.txt'

start_wall_time = time.time()
start_cpu_time = time.process_time()

with open(INPUT_FILE) as f:
    content = f.read()

print("assembling tile list")
tiles = [ Point( map(int, xy.split(",")) ) for xy in content.splitlines()]
print("done.")
print("generating boundary")
boundary = Polygon(tiles)
print("done.")

print("calculating all rectangle sizes")
# calculate all rectangle sizes
sizes: dict[tuple[Point, Point], float] = {}
for idx, tile1 in enumerate(tiles[:-1], 1):
    for tile2 in tiles[idx:]:
        sizes[(tile1, tile2)] = (abs(tile2.x - tile1.x) + 1) * (abs(tile2.y - tile1.y) + 1)
print("done.")

print("sorting by rectangle size")
sorted_points = sorted(sizes, key=lambda pair: sizes[pair], reverse=True)
print("done.")

print("checking for containment")
for tile1, tile2 in sorted_points:
    # tile_mid & end works because we don't care if the polygon is clockwise or counter-
    tile_mid = Point(tile1.x, tile2.y)
    tile_end = Point(tile2.x, tile1.y)
    rect = Polygon([tile1, tile_mid, tile2, tile_end])
    if boundary.contains(rect):
        print(f"max size: {sizes[(tile1, tile2)]:.0f}")
        break
print("done.")

elapsed_wall_time = time.time() - start_wall_time
elapsed_cpu_time = time.process_time() - start_cpu_time
print(f"took {elapsed_wall_time:.3f} seconds / {elapsed_cpu_time:.3f} cpu seconds")