import unittest
import power

class TestPowerMethods (unittest.TestCase):
    def test_calculate_power_from_steps(self):
        number_of_steps = 25
        pw = power.power()
        result = pw.calculatePowerFromSteps(number_of_steps)
        self.assertEqual(result, 0.0028)
        

