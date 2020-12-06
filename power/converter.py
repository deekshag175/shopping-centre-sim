# This is a simulation and we want inputs as parameters
import sys
import random
import logging
import power.shopping_centre

class converter:
    def is_integer(self, n):
        try:
            int(n)
        except ValueError:
            return False
        else:
            return True

    def generatePeopleSteps(self, number_of_people):
        all_power = []
        for x in range(1, number_of_people):
            step_count = random.randint(2000, 15000)
            power, price = calculatePricePowerByStepCount(step_count)
            all_power.append(power)
        return sum(all_power)
 
if __name__ == '__main__':
    cnv = converter()
    if (len(sys.argv) > 1) and cnv.is_integer(sys.argv[1]):
        number_of_people = int(sys.argv[1])
        sc = shopping_centre.shopping_centre(number_of_people)
        sc.draw()
    else:
        print("Usage: python converter.py [number_of_people]")        