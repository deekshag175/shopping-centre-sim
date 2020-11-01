# This is a simulation and we want inputs as parameters
import sys
import random
import logging
import shopping_centre


def generatePeopleSteps(number_of_people):
    all_power = []
    for x in range(1, number_of_people):
        step_count = random.randint(2000, 15000)
        power, price = calculatePricePowerByStepCount(step_count)
        all_power.append(power)
    return sum(all_power)
 
if __name__ == '__main__':
    # TODO: Add exception handling to check the inputs and make sure that we have 3 values
    
    #number_of_people = int(sys.argv[1])
    number_of_people = 10
    """
    total_power = generatePeopleSteps(number_of_people)
    total_power_price = total_power * price_conversion_rate_per_kw
    print("\n\n You saved £{:,.2f} and generated {:,.2f} KWH ".format((total_power_price), float(total_power)))
    """
    sc = shopping_centre.shopping_centre(number_of_people)
    sc.draw()