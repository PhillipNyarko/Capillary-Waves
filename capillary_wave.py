import time
import math
from ripple import Ripple


class CapillaryWave:
    def __init__(self, mouse_position, window, color, shadow_color, background_color):
        self.mouse_position = mouse_position
        self.ripples_list = []
        self.window = window
        self.color = color
        self.shadow_color = shadow_color
        self.background_color = background_color

        # initialize all the ripples witha radius of 0
        self.number_of_ripples = 8 
        for i in range(self.number_of_ripples):
            new_ripple = Ripple(self.mouse_position, 0, self.color, self.shadow_color)
            self.ripples_list.append(new_ripple)

        number_of_frames = 75
        for i in range(1, number_of_frames + 1):

            self.ripples_list[-1].radius += i ** 2 # increase the radius of the last ripple in the ripple list

            # set the positions of each ripple to be the square root of the next ripple in the ripple list
            for j in range(len(self.ripples_list) - 2, -1, -1):
                self.ripples_list[j].radius = (self.ripples_list[j + 1].radius) / 2

            # draw all the ripples
            for j in range(len(self.ripples_list)):
                self.ripples_list[j].draw(self.window)

            # pause temporarily and clear the window  

            self.window.fill(self.background_color)
            time.sleep(0.1)

