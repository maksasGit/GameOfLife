import pygame
from world import World

window_size = (1000 , 800)
cell_size = 6



pygame.init()
display = pygame.display.set_mode((window_size[0] , window_size[1]))
clock = pygame.time.Clock()
world = World( int(window_size[0] / cell_size) , int(window_size[1] / cell_size))

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
    world.update()
    for i in range(world.world_size[0]):
        for j in range(world.world_size[1]):
            color = (50, 50, 50) if world.world[i][j] == 0 else (0, 0, 0)
            pygame.draw.rect(display, color, (i * cell_size, j * cell_size, cell_size, cell_size))
    pygame.display.update()
    clock.tick(8)
