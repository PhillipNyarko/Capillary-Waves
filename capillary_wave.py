import time
import math
from ripple import Ripple

# colors
BACKGROUND_COLOR = (25, 25, 25)
BLUE = (78, 104, 235)

class CapillaryWave:
    def __init__(self, mouse_position, window):
        self.mouse_position = mouse_position
        self.color = BLUE 
        self.ripples_list = []
        self.window = window

        # initialize all the ripples witha radius of 0
        for i in range(10):
            new_ripple = Ripple(self.mouse_position, 0, self.color)
            self.ripples_list.append(new_ripple)

        number_of_frames = 100
        for i in range(1, number_of_frames + 1):

            self.ripples_list[-1].radius += i ** 2 # increase the radius of the last ripple in the ripple list

            # set the positions of each ripple to be the square root of the next ripple in the ripple list
            for j in range(len(self.ripples_list) - 2, -1, -1):
                self.ripples_list[j].radius = (self.ripples_list[j + 1].radius) / 2
                print(self.ripples_list[j].radius)
            print("_____")

            # draw all the ripples
            for j in range(len(self.ripples_list)):
                self.ripples_list[j].draw(self.window)

            # pause temporarily and clear the window  

            self.window.fill(BACKGROUND_COLOR)
            time.sleep(0.05)

