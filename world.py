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
        new_world = self.world.copy()
        mask1 = (self.world == 1) & ((neighbors == 2) | (neighbors == 3))
        mask2 = (self.world == 0) & (neighbors == 3)
        new_world[mask1] = 0
        new_world[mask2] = 1
        self.world = new_world
        return new_world
