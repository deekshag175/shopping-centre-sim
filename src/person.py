from pygame import Rect
import pygame

class person:

    def __init__(self, surface, posx, posy, numsteps):
        self.posx = posx
        self.posy = posy
        self.numsteps = numsteps
        self.surface = surface
        self.person_shopping = pygame.image.load('person_shopping.png')
        self.check_screen_pos()

    def draw(self, posx):
        self.surface.blit(self.person_shopping, (posx, self.posy))
        pygame.display.update()
        print("{},{}".format(posx, self.posy))
    
    def move(self):
        pygame.draw.rect(self.surface, (0, 0, 0), (self.posx, self.posy, 32, 32))
        if self.posx > 1280: self.posx = 0
        self.posx = self.posx + 32
        self.draw(self.posx)

    def check_screen_pos(self):
        if self.posy > 736: # This is 768 which is the screen height - the size of the shopper graphic
            self.posy = 736
        
    # TODO: write a function that checks whether each shopper is in the space of another shopper