import numpy as np
import scipy.ndimage # type: ignore

INPUT_FILE = 'day-4 input.txt'

with open(INPUT_FILE) as f:
    content = f.read()

value_map = {
    '@': 1,
    '.': 0
}

array = [ [ value_map[cell] for cell in row ] for row in content.split("\n") ]

start_grid = np.array(array)

# 3x3 kernel for Moore neighborhood (8 neighbors)
kernel = np.array([[1,1,1],
                   [1,0,1],
                   [1,1,1]])

total_removed = 0
while True:
    neighbor_counts = scipy.ndimage.convolve(start_grid, kernel, mode='constant', cval=0) # type: ignore
    filtered = scipy.ndimage.generic_filter(neighbor_counts, lambda x: 1 if x < 4 else 0, 1) # type: ignore
    masked = filtered * start_grid # type: ignore
    removable = scipy.ndimage.sum_labels(masked) # type: ignore
    if removable == 0:
        break
    total_removed += removable
    start_grid = start_grid * (masked^1) # type: ignore

print(f"{total_removed=}")