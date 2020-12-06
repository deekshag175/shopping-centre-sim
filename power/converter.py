# This is a simulation and we want inputs as parameters
import sys
import random
import logging
import shopping_centre

def is_integer(n):
    try:
        int(n)
    except ValueError:
        return False
    else:
        return True

def generatePeopleSteps(number_of_people):
    all_power = []
    for x in range(1, number_of_people):
        step_count = random.randint(2000, 15000)
        power, price = calculatePricePowerByStepCount(step_count)
        all_power.append(power)
    return sum(all_power)
 
if __name__ == '__main__':
    if (len(sys.argv) > 1) and is_integer(sys.argv[1]):
        number_of_people = int(sys.argv[1])
        sc = shopping_centre.shopping_centre(number_of_people)
        sc.draw()
    else:
        print("Usage: python converter.py [number_of_people]")        