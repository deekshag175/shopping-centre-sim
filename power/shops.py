from pygame import Rect
import pygame, os

class shops:

    def __init__(self, shpygame):
        self.shops_pygame = shpygame

    def draw_to_screen(self):
        # (1280 / 4) / 3 - used as the 4 shops and starting a third of the way into the image
        self.shopnum = int(self.shops_pygame.image_uri[0])
        self.posx = ((self.shopnum - 1) * 320) + 140
        self.posy = 50
        if self.shopnum > 4: 
            self.posx = ((self.shopnum - 5) * 320) + 140
            self.posy = 678
        print("shop number: {} with position ({},{})".format(self.shopnum, self.posx, self.posy))
        self.shops_pygame.draw_to_screen(self.posx, self.posy)
        

class shops_pygame:

    def __init__(self, surface, image_uri):
        self.image_uri = image_uri
        self.surface = surface
        self.store_logo = pygame.image.load("power\\images\\" + image_uri)

    def draw_to_screen(self, posx, posy):
        self.surface.blit(self.store_logo, (posx, posy))
        pygame.display.update()