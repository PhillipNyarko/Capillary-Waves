import pygame

class Ripple:
    def __init__(self, mouse_position, radius, color):
        self.mouse_position = mouse_position
        self.radius = radius
        self.color = color

    def draw(self, window):
        pygame.draw.circle(window, self.color, self.mouse_position, self.radius, width=2)
        pygame.display.update()
