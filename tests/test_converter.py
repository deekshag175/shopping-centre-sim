import pytest
from power.converter import converter

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


