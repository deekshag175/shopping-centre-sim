import pygame
from power.power import power
from power.shops import shops, shops_pygame
from power.person import person, person_pygame
import random
import sys, os

class shopping_centre:
    
    def __init__(self, numpeople):
        self.width = 1280
        self.height = 798
        self.numshops = 10
        self.numpeople = numpeople
        self.step_counter = 0
        self.seconds_counter = 0
        self.displayobj = shopping_centre_pygame(self.width, self.height)
        self.display = None
        self.pers_pygame = None
        self.all_shops = []
        
    def init_power_text(self):
        self.display = self.displayobj.build_display_caption()
        self.pers_pygame = person_pygame(self.display)
        textsurface, myfont = self.displayobj.init_power_text()
        # create our power object
        return power(), textsurface, myfont

    def draw_shops(self):
        self.displayobj.draw_internal_shops_1()
        logos = ['1_nike_logo.png', '2_subway_logo.png', '3_sportdirect_logo.png', '4_apple_logo.png', \
            '5_waterstones_logo.png', '6_primark_logo.png', '7_tesco_logo.png', '8_boots_logo.png']
        [self.all_shops.append(self.displayobj.draw_internal_shops_2(logo)) for logo in logos]
        
    def draw(self):
        _power, textsurface, myfont = self.init_power_text()
        self.draw_shops()

        # TODO: Deeksha to define number of steps as an input mechanism for each person - maybe randomise up front
        # Adding shopping centre channel in the middle of the screen 150px up top and 150px at the bottom
        allpeople = [person(self.pers_pygame, random.randint(0, self.width), random.randint(150, self.height - 210), p) \
            for p in range (self.numpeople + 1)]

        for i in range(0, len(allpeople)):
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
            self.display.fill((0, 0, 0), (0, 768, 1280, 30))
            price, powerout = _power.calculatePricePowerByStepCount(self.step_counter)
            textsurface = myfont.render('Time: {} seconds | Steps: {} | Cumulative Power: {} KW, | Cost Savings: £{}'.format(str(self.seconds_counter), str(self.step_counter), str(round(powerout, 3)), str(round(price, 2)).zfill(2)), True, (255, 255, 255))
            self.display.blit(textsurface, (0, 768))
            pygame.time.wait(1000)
            pygame.display.update()
            self.seconds_counter = self.seconds_counter + 1

class shopping_centre_pygame:

    def __init__(self, width, height):
        self.width = width 
        self.height = height
        self.display = None

    def init_power_text(self):
        # initiate the font loader
        pygame.font.init()
        myfont = pygame.font.SysFont('Comic Sans MS', 16)
        textsurface = myfont.render('Steps: 0', True, (255, 255, 255))
        # Label the shops at the top of the screen
        myfont_shops = pygame.font.SysFont('Comic Sans MS', 48)
        textsurface_shops = myfont.render('Shops', True, (255, 255, 255))
        self.display.blit(textsurface_shops, (0, 10))
        return textsurface, myfont

    def build_display_caption(self):
        display_mode = pygame.display.set_mode((self.width, self.height))
        pygame.display.set_caption("Shopping Centre Simulator")
        pygame.init()
        self.display = display_mode
        return self.display

    def draw_internal_shops_1(self):
        # Draw in the shops at the top of the screen
        pygame.draw.line(self.display, (255, 255, 255), (0, 150), (1280, 150))
        pygame.display.flip()
        # Draw in the shops at the bottom of the screen
        pygame.draw.line(self.display, (255, 255, 255), (0, 618), (1280, 618))
        pygame.display.flip()

    def draw_internal_shops_2(self, logo):
        shop = shops(shops_pygame(self.display, logo))
        shop.draw_to_screen()
        return shop

    def draw(self):
        pass