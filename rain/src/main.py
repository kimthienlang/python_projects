import pygame
import random
from particle import Particle

pygame.init()

width = 800
height = 600
window_size = (width, height)
window_color = "light blue"

window = pygame.display.set_mode(window_size)
pygame.display.set_caption("Game Window")
clock = pygame.time.Clock()
##
img = pygame.image.load('../img/bg.png')
img = pygame.transform.scale(img, (width, height))
rains = []
for i in range(0, 100):
    rain_width = random.uniform(0, width)
    rain_height = random.uniform(-5, 0)
    rains.append(Particle(rain_width, rain_height))
##
running = True
while running:
    window.blit(img, (0, 0))
    print("GAME Running")
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    for o in rains:
        o.update()
        o.show(window)

    pygame.display.update()
    clock.tick(120) #120 FPS

pygame.quit()