import pygame

class Ripple:
    def __init__(self, mouse_position, radius, color, shadow_color):
        self.mouse_position = mouse_position
        self.radius = radius
        self.color = color
        self.width = 8
        self.shadow_color = shadow_color
        self.shadow_width = 20

    def draw(self, window):
        pygame.draw.circle(window, self.color, self.mouse_position, self.radius, width=self.width)
        pygame.draw.circle(window, self.shadow_color, self.mouse_position, self.radius-1, width=self.shadow_width)
        pygame.display.update()
