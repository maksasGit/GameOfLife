# import numpy as np
# import matplotlib.pyplot as plt
# import matplotlib.animation as animation
#
# world_size = (500, 500)
# world = np.random.choice([0, 1], size=world_size, p=[0.7, 0.3])
#
# # Precompute the indices of the neighbors
# neighbor_indices = np.array([
#     [-1, -1], [-1, 0], [-1, 1],
#     [0, -1], [0, 1],
#     [1, -1], [1, 0], [1, 1]
# ])
#
# def update_world(frame_number, world, world_size, neighbor_indices):
#     # Compute the number of neighbors for each cell
#     neighbors = np.zeros_like(world)
#     for i in range(8):
#         neighbors += np.roll(world, neighbor_indices[i], axis=(0, 1))
#
#     # Apply the rules of the Game of Life
#     new_world = np.zeros_like(world)
#     new_world[np.logical_and(world == 1, np.logical_or(neighbors == 2, neighbors == 3))] = 1
#     new_world[np.logical_and(world == 0, neighbors == 3)] = 1
#
#     # Update the image data
#     mat.set_data(new_world)
#
#     # Update the world array
#     np.copyto(world, new_world)
#
#     # Return the image object as a list
#     return [mat]
#
# # Create the animation
# fig, ax = plt.subplots()
# mat = ax.imshow(world, cmap='gray')
# plt.gca().invert_yaxis()
# ani = animation.FuncAnimation(fig, update_world, fargs=(world, world_size, neighbor_indices), frames=100, blit=True)
# manager = plt.get_current_fig_manager()
# manager.full_screen_toggle()
# plt.show()


import pygame
import numpy as np

# Define the world size and cell size
world_size = (100, 100)
cell_size = 5

# Create the Pygame window
pygame.init()
screen = pygame.display.set_mode(world_size, pygame.FULLSCREEN)
clock = pygame.time.Clock()
pygame.display.set_caption("Game of Life")

# Generate the initial world state
world = np.random.choice([0, 1], size=world_size, p=[0.7, 0.3])

# Precompute the indices of the neighbors
neighbor_indices = np.array([
    [-1, -1], [-1, 0], [-1, 1],
    [0, -1], [0, 1],
    [1, -1], [1, 0], [1, 1]
])

# Define the update function
def update_world(world, neighbor_indices):
    # Compute the number of neighbors for each cell
    neighbors = np.zeros_like(world)
    for i in range(8):
        neighbors += np.roll(world, neighbor_indices[i], axis=(0, 1))

    # Apply the rules of the Game of Life
    new_world = np.zeros_like(world)
    new_world[np.logical_and(world == 1, np.logical_or(neighbors == 2, neighbors == 3))] = 1
    new_world[np.logical_and(world == 0, neighbors == 3)] = 1

    # Update the world array
    np.copyto(world, new_world)

# Define the render function
def render_world(world, screen):
    # Clear the screen
    screen.fill((255, 255, 255))

    # Draw the live cells
    rows, cols = np.where(world == 1)
    for row, col in zip(rows, cols):
        rect = pygame.Rect(col * cell_size, row * cell_size, cell_size, cell_size)
        pygame.draw.rect(screen, (0, 0, 0), rect)

    # Update the display
    pygame.display.flip()

# Run the simulation
running = True
while running:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Update the world state
    update_world(world, neighbor_indices)

    # Render the world
    render_world(world, screen)

# Quit Pygame
pygame.quit()
