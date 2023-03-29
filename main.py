import pygame
from world import World

pygame.init()
display = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
clock = pygame.time.Clock()
world = World(1920,1080)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
    world.update()
    display.blit(pygame.surfarray.make_surface(world.world), (0, 0))
    pygame.display.update()
    clock.tick(144)
