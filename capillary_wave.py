import time
from ripple import Ripple

class CapillaryWave:
    def __init__(self, mouse_position, color, window):
        self.mouse_position = mouse_position
        self.color = color
        self.ripples_list = [Ripple(self.mouse_position, 0, self.color)] * 5
        self.window = window

        print("drawing capillary wave starting @" + str(self.mouse_position))

        for j in range(len(self.ripples_list)):
            self.ripples_list[j].radius = (self.ripples_list[i - 1].radius ** 2) -10

        # draw all the ripples in one frame
        for j in range(len(self.ripples_list)):
            self.ripples_list[i].draw(self.window)
            time.sleep(0.5)
            self.window.fill((0,0,0))
            


