import pygame
class shopping_centre:
    def __init__(self):
        self.width = 1280
        self.height = 768
        self.numshops = 10
    def draw(self):
        displaysize = pygame.display.set_mode((self.width, self.height))
        pygame.display.set_caption("Shopping Centre Simulator")
        pygame.init()
        
        
