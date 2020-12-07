import pytest
from power.power import power
from person.person import person
from power.converter import converter
import power.shopping_centre 

def test_is_integer_true():
    myint = "25"
    cnv = converter()
    result = cnv.is_integer(myint)
    assert result == True

def test_is_integer_false():
    myint = "2x"
    cnv = converter()
    result = cnv.is_integer(myint)
    assert result == False


