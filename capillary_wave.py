import time
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

        number_of_frames = 10
        for i in range(1, number_of_frames + 1):

            self.ripples_list[-1].radius += i ** 2 # increase the radius of the last ripple in the ripple list
                #DOESN'T WORK THEY'LL ALL END UP BEING "2" FIX LATER 

            # set the positions of each ripple for the current frame
            for j in range(len(self.ripples_list)):
                self.ripples_list[j].radius = self.ripples_list[j - 1].radius 

            # draw all the ripples
            for j in range(len(self.ripples_list)):
                self.ripples_list[j].draw(self.window)

            # pause temporarily and clear the window  
            time.sleep(0.01)
            self.window.fill(BACKGROUND_COLOR)
                


