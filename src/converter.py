# This is a simulation and we want inputs as parameters
import sys
import random
import logging
import shopping_centre
price_conversion_rate_per_kw = 0.1437
number_of_Steps_per_KWH = 8800
 
def calculatePowerFromSteps( number_of_steps):
    """ 
    This function calculates power from steps.
    Power is measured in Watts
    Force is measured in Newtons
 
    Parameters
    ----------
    weight : float, mandatory
            The weight of the person walking on the tile
    number_of_steps : float, mandatory
            Number of steps within a period of time
    time_in_minutes : float, optional 
            Number of minutes taken to achieve these steps
    """
    power = number_of_Steps_per_KWH/number_of_steps
    print("DEBUG: Total power {} KWH".format(power))
    return power
 
def calculatePriceFromPower(power):
    price = power * price_conversion_rate_per_kw
    return price
 
def calculatePricePowerByStepCount(number_of_steps):
    power = calculatePowerFromSteps(number_of_steps)
    price = calculatePriceFromPower(power)
    print("DEBUG: You saved £{} and generated {} KWH ".format(str(price).zfill(2), float(power)))
    return power, price

def generatePeopleSteps(number_of_people):
    all_power = []
    for x in range(1, number_of_people):
        step_count = random.randint(2000, 15000)
        power, price = calculatePricePowerByStepCount(step_count)
        all_power.append(power)
    return sum(all_power)
 
if __name__ == '__main__':
    # TODO: Add exception handling to check the inputs and make sure that we have 3 values
    """
    number_of_people = int(sys.argv[1])
    total_power = generatePeopleSteps(number_of_people)
    total_power_price = total_power * price_conversion_rate_per_kw
    print("\n\n You saved £{:,.2f} and generated {:,.2f} KWH ".format((total_power_price), float(total_power)))
    """
    sc = shopping_centre.shopping_centre()
    sc.draw()


