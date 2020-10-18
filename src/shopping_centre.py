import pygame

class shopping_centre:
    
    def __init__(self, numpeople):
        self.width = 1280
        self.height = 768
        self.numshops = 10
        self.numpeople = numpeople
        
    def draw(self):
        displaysize = pygame.display.set_mode((self.width, self.height))
        pygame.display.set_caption("Shopping Centre Simulator")
        pygame.init()

        allpeople = [person(1,1,p) for p in range (numpeople)]
        
        while True:
            for i in len(allpeople):
                allpeople[i].draw()
            
        
