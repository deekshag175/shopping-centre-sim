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

        # TODO: Deeksha to define number of steps as an input mechanism for each person - maybe randomise up front
        allpeople = [person.person(displaysize, random.randint(0,self.width), random.randint(0,self.height), p) \
            for p in range (self.numpeople)]

        for i in range(0, len(allpeople)-1):
            allpeople[i].draw(allpeople[i].posx)
            print(str(i))

        while True:
            for event in pygame.event.get():
                # TODO: Deeksha to add an event to the game so that if someone presses the Q button it quits
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                for i in range(0, len(allpeople)-1):
                    for j in range(0, 10):
                        allpeople[i].move()
            pygame.display.update()
            # TODO: Deeksha to create a new score counter which will update on each go with an increment of people * steps * energy value = GBP


        
