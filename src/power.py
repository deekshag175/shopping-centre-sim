class power:

    price_conversion_rate_per_kw = 0.1437
    number_of_Steps_per_KWH = 8800
    
    def calculatePowerFromSteps(self, number_of_steps):
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
        power = float(number_of_steps / self.number_of_Steps_per_KWH)
        print("DEBUG: Total power {} KWH".format(power))
        return power
    
    def calculatePriceFromPower(self, power):
        price = power * self.price_conversion_rate_per_kw
        return price
    
    def calculatePricePowerByStepCount(self, number_of_steps):
        power = self.calculatePowerFromSteps(number_of_steps)
        price = self.calculatePriceFromPower(power)
        print("DEBUG: You saved £{} and generated {} KWH ".format(str(price).zfill(2), float(power)))
        return power, price