import pygame
import power.person, power.power, power.shops
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

    def __init_power_text(self, shopping_centre_display):
        # initiate the font loader
        pygame.font.init()
        myfont = pygame.font.SysFont('Comic Sans MS', 16)
        textsurface = myfont.render('Steps: 0', True, (255, 255, 255))
        # create our power object
        _power = power.power()
        # Label the shops at the top of the screen
        myfont_shops = pygame.font.SysFont('Comic Sans MS', 48)
        textsurface_shops = myfont.render('Shops', True, (255, 255, 255))
        shopping_centre_display.blit(textsurface_shops, (0, 10))
        return _power, textsurface, myfont

    def __draw_internal_shops(self, shopping_centre_display):
        # Draw in the shops at the top of the screen
        pygame.draw.line(shopping_centre_display, (255, 255, 255), (0, 150), (1280, 150))
        pygame.display.flip()
        # Draw in the shops at the bottom of the screen
        pygame.draw.line(shopping_centre_display, (255, 255, 255), (0, 618), (1280, 618))
        pygame.display.flip()
        
        all_shops = []
        all_shops.append(shops.shops(shopping_centre_display, '1_nike_logo.png'))
        all_shops.append(shops.shops(shopping_centre_display, '2_subway_logo.png'))
        all_shops.append(shops.shops(shopping_centre_display, '3_sportdirect_logo.png'))
        all_shops.append(shops.shops(shopping_centre_display, '4_apple_logo.png'))
        all_shops.append(shops.shops(shopping_centre_display, '5_waterstones_logo.png'))
        all_shops.append(shops.shops(shopping_centre_display, '6_primark_logo.png'))
        all_shops.append(shops.shops(shopping_centre_display, '7_tesco_logo.png'))
        all_shops.append(shops.shops(shopping_centre_display, '8_boots_logo.png'))
        for x in all_shops:
            x.draw_to_screen()
        
    def draw(self):
        displaysize = pygame.display.set_mode((self.width, self.height))
        pygame.display.set_caption("Shopping Centre Simulator")
        pygame.init()

        _power, textsurface, myfont = self.__init_power_text(displaysize)
        self.__draw_internal_shops(displaysize)

        # TODO: Deeksha to define number of steps as an input mechanism for each person - maybe randomise up front
        # Adding shopping centre channel in the middle of the screen 150px up top and 150px at the bottom
        allpeople = [person.person(displaysize, random.randint(0, self.width), random.randint(150, self.height - 210), p) \
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
            displaysize.fill((0, 0, 0), (0, 768, 1280, 30))
            price, powerout = _power.calculatePricePowerByStepCount(self.step_counter)
            textsurface = myfont.render('Time: {} seconds | Steps: {} | Cumulative Power: {} KW, | Cost Savings: £{}'.format(str(self.seconds_counter), str(self.step_counter), str(round(powerout, 3)), str(round(price, 2)).zfill(2)), True, (255, 255, 255))
            displaysize.blit(textsurface, (0, 768))
            pygame.time.wait(1000)
            pygame.display.update()
            self.seconds_counter = self.seconds_counter + 1