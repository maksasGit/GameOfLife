import numpy as np

neighbor_indices = np.array([
    [-1, -1], [-1, 0], [-1, 1],
    [0, -1], [0, 1],
    [1, -1], [1, 0], [1, 1]
])

class World:
    def __init__(self, width, height):
        self.world_size = (width, height)
        self.world = np.random.choice([0 , 1], size=self.world_size, p=[0.7, 0.3])



    def update(self):
        neighbors = np.zeros_like(self.world)
        for curr_neighbors in neighbor_indices:
            neighbors += np.roll(self.world, curr_neighbors, axis=(0, 1))
        new_world = np.zeros_like(self.world)
        new_world[np.logical_and(self.world == 1, np.logical_or(neighbors == 2, neighbors == 3))] = 1
        new_world[np.logical_and(self.world == 0, neighbors == 3)] = 1

        np.copyto(self.world, new_world)
        return new_world
