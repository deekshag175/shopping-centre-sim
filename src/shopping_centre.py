import pygame
import person
import random
import sys

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

        allpeople = [person.person(displaysize,random.randint(0,self.width),random.randint(0,self.height),p) for p in range (self.numpeople)]

        
        for i in range(0, len(allpeople)-1):
            allpeople[i].draw()
            print(str(i))

        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
            pygame.display.update()
        
