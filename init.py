# This is a simulation and we want inputs as parameters
import sys
import random
import logging
from power.shopping_centre import shopping_centre
from power.converter import converter

if __name__ == '__main__':
    cnv = converter()
    if (len(sys.argv) > 1) and cnv.is_integer(sys.argv[1]):
        number_of_people = int(sys.argv[1])
        sc = shopping_centre(number_of_people)
        sc.draw()
    else:
        print("Usage: python init.py [number_of_people]")      