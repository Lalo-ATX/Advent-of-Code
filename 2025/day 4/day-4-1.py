import numpy as np
import scipy.ndimage as snd # type: ignore

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

neighbor_counts = snd.convolve(start_grid, kernel, mode='constant', cval=0) # type: ignore
filtered = snd.generic_filter(neighbor_counts, lambda x: 1 if x < 4 else 0, 1) # type: ignore
masked = filtered * start_grid # type: ignore
count = snd.sum_labels(masked) # type: ignore
print(f"{count=}")