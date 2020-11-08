import pygame
import person, power
import random
import sys

class shopping_centre:
    
    def __init__(self, numpeople):
        self.width = 1280
        self.height = 798
        self.numshops = 10
        self.numpeople = numpeople
        self.step_counter = 0
        self.seconds_counter = 0
        
    def draw(self):
        displaysize = pygame.display.set_mode((self.width, self.height))
        pygame.display.set_caption("Shopping Centre Simulator")
        pygame.init()

        pygame.font.init()
        myfont = pygame.font.SysFont('Comic Sans MS', 16)
        textsurface = myfont.render('Steps: 0', True, (255, 255, 255))

        _power = power.power()

        # TODO: Deeksha to define number of steps as an input mechanism for each person - maybe randomise up front
        allpeople = [person.person(displaysize, random.randint(0,self.width), random.randint(0,self.height), p) \
            for p in range (self.numpeople)]

        for i in range(0, len(allpeople)-1):
            allpeople[i].draw(allpeople[i].posx)
            print(str(i))

        while True:
            for event in pygame.event.get():
                if (event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_q)):
                    pygame.quit()
                    sys.exit()
            for i in range(0, len(allpeople)-1):
                allpeople[i].move()
                self.step_counter = self.step_counter + 1
            # TODO: Deeksha to create a new score counter which will update on each go with an increment of people * steps * energy value = GBP    
            displaysize.fill((0, 0, 0), (0, 768, 1280, 30))
            price, powerout = _power.calculatePricePowerByStepCount(self.step_counter)
            textsurface = myfont.render('Time: {} seconds | Steps: {} | Cumulative Power: {} KW, | Cost Savings: £{}'.format(str(self.seconds_counter), str(self.step_counter), str(round(powerout, 3)), str(round(price, 2)).zfill(2)), True, (255, 255, 255))
            displaysize.blit(textsurface, (0, 768))
            pygame.time.wait(1000)
            pygame.display.update()
            self.seconds_counter = self.seconds_counter + 1