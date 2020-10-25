from pygame import Rect
import pygame

class person:

    def __init__(self, surface, posx, posy, numsteps):
        self.posx = posx
        self.posy = posy
        self.numsteps = numsteps
        self.surface = surface

    def draw(self):
        WHITE =(255,255,255)
        BLUE =(0,0,255)
        person_shopping = pygame.image.load('person_shopping.png')
        person_rect = Rect(self.posx, self.posy, 8, 8)
        self.surface.blit(person_shopping, (self.posx, self.posy))
        pygame.display.update()
        print("{},{}".format(self.posx, self.posy))
        
