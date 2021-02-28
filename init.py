# This is a simulation and we want inputs as parameters
import sys
import random
import logging
from power.shopping_centre import shopping_centre
from power.converter import converter
import simulation
import asyncio

if __name__ == '__main__':
    cnv = converter()
    if (len(sys.argv) == 2) and (int(sys.argv[1]) == 0):
        sim = simulation.simulation(1)
        loop = asyncio.get_event_loop()
        loop.run_until_complete(sim.generate_event())
    elif (len(sys.argv) == 3) and cnv.is_integer(sys.argv[2]) and cnv.is_integer(sys.argv[1]):
        number_of_people = int(sys.argv[2])
        sc = shopping_centre(number_of_people)
        sc.draw()
    else:
        print("Usage: python init.py [sim_type] [number_of_people]")      