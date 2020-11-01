from pygame import Rect
import pygame

class person:

    def __init__(self, surface, posx, posy, numsteps):
        self.posx = posx
        self.posy = posy
        self.numsteps = numsteps
        self.surface = surface
        self.person_shopping = pygame.image.load('person_shopping.png')

    def draw(self, posx):
        self.surface.blit(self.person_shopping, (posx, self.posy))
        pygame.display.update()
        print("{},{}".format(posx, self.posy))
    
    # TODO: Deeksha to create a draw method which will move the shoppers along a square at a time
    def move(self):
        prev_pos = self.person_shopping.get_rect()
        self.posx = self.posx + 32
        self.draw(self.posx)
        pygame.draw.rect(self.surface, (0, 0, 0), prev_pos)
        pygame.display.update()