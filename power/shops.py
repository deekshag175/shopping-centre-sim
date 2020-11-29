from pygame import Rect
import pygame, os

class shops:

    def __init__(self, surface, image_uri):
        self.image_uri = image_uri
        self.surface = surface
        self.store_logo = pygame.image.load("images\\" + image_uri)

    def draw_to_screen(self):
        # (1280 / 4) / 3 - used as the 4 shops and starting a third of the way into the image
        shopnum = int(self.image_uri[0])
        posx = ((shopnum - 1) * 320) + 140
        posy = 50
        if shopnum > 4: 
            posx = ((shopnum - 5) * 320) + 140
            posy = 678
        print("shop number: {} with position ({},{})".format(shopnum, posx, posy))
        self.surface.blit(self.store_logo, (posx, posy))
        pygame.display.update()