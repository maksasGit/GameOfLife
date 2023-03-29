import pygame
from world import World

pygame.init()
display = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
clock = pygame.time.Clock()
window_size = (1920 , 1080)
CELL_SIZE = 6
world = World( int(window_size[0] / CELL_SIZE) , int(window_size[1] / CELL_SIZE))

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
    world.update()
    for i in range(world.world_size[0]):
        for j in range(world.world_size[1]):
            color = (50, 50, 50) if world.world[i][j] == 0 else (0, 0, 0)
            pygame.draw.rect(display, color, (i * CELL_SIZE, j * CELL_SIZE, CELL_SIZE, CELL_SIZE))
    pygame.display.update()
    clock.tick(8)
