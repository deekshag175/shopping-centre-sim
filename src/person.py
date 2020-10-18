import pygame

class person:

    def __init__(self, posx, posy, numsteps):
        self.posx = posx
        self.posy = posy
        self.numsteps = numsteps

    def draw(self):
        pygame.draw.line(surface, (255,255,255), (self.posx, self.posy), (self.posx, self.posy))
