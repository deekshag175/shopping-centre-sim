import pytest
from src.power import power

def test_calculate_power_from_steps():
    number_of_steps = 25
    pw = power()
    result = pw.calculatePowerFromSteps(number_of_steps)
    assert result == 0.0028