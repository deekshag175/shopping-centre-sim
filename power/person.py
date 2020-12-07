from pygame import Rect
import pygame

class person:

    def __init__(self, pers_pygame, posx, posy, numsteps):
        self.posx = posx
        self.posy = posy
        self.numsteps = numsteps
        self.pers_pygame = pers_pygame
        self.check_screen_pos()

    def draw(self, posx):
        self.pers_pygame.process_draw(posx, self.posy)
    
    def move(self):
        self.pers_pygame.process_move(self.posx, self.posy)
        if self.posx > 1280: self.posx = 0
        self.posx = self.posx + 32
        self.draw(self.posx)

    def check_screen_pos(self):
        if self.posy > 736: # This is 768 which is the screen height - the size of the shopper graphic
            self.posy = 736
        
    # TODO: write a function that checks whether each shopper is in the space of another shopper

class person_pygame:

    def __init__(self, surface):
        self.person_shopping = pygame.image.load('power/images/person_shopping.png')
        self.surface = surface

    def process_draw(self, posx, posy):
        self.surface.blit(self.person_shopping, (posx, posy))
        pygame.display.update()
        print("{},{}".format(posx, posy))

    def process_move(self, posx, posy):
        pygame.draw.rect(self.surface, (0, 0, 0), (posx, posy, 32, 32))