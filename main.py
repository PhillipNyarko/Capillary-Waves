import sys
import time
import pygame
from capillary_wave import CapillaryWave 

pygame.init()

window_width, window_height = 600, 500
window_size = (window_width, window_height)
window = pygame.display.set_mode(window_size)

pygame.display.set_caption("Water Ripples")

BACKGROUND_COLOR = (25, 25, 25) 

# game loop

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if event.type == pygame.MOUSEBUTTONDOWN:
            if pygame.mouse.get_pressed()[0]: # if left mouse button pressed
                capillary_wave = CapillaryWave(pygame.mouse.get_pos(), window)

    window.fill(BACKGROUND_COLOR) # fill background
    pygame.display.update() # update display
    pygame.time.Clock().tick() # set max frames-per-second

