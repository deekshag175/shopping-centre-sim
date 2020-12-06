import pytest
from power.power import power

def test_calculate_power_from_steps():
    number_of_steps = 25
    pw = power()
    result = pw.calculatePowerFromSteps(number_of_steps)
    assert result == 0.0028

def test_price_from_power():
    power_in_kW = 1.0
    pw = power()
    result = pw.calculatePriceFromPower(power_in_kW)
    assert result == 0.1437

def test_calculate_pricepower_by_stepcount():
    number_of_steps = 100000
    pw = power()
    result1, result2 = pw.calculatePricePowerByStepCount(number_of_steps)
    assert round(result1, 2) == 11.36
    assert round(result2, 2) == 1.63