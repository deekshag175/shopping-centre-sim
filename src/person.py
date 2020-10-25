from pygame import Rect
import pygame

class person:

    def __init__(self, surface, posx, posy, numsteps):
        self.posx = posx
        self.posy = posy
        self.numsteps = numsteps
        self.surface = surface

    def draw(self):
        person_shopping = pygame.image.load('person_shopping.png')
        self.surface.blit(person_shopping, (self.posx, self.posy))
        pygame.display.update()
        print("{},{}".format(self.posx, self.posy))
    
    # TODO: Deeksha to create a draw method which will move the shoppers along a square at a time
