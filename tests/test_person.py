import pytest
from power.person import person

def test_shopper_posx_out_of_bounds():
    p = person(person_pygame_fake(None), 1281, 0, 25)
    p.move()
    assert p.posx == 32

def test_shopper_posx_move_forward():
    p = person(person_pygame_fake(None), 100, 0, 25)
    p.move()
    assert p.posx == 132

def test_screen_posy_bounds_over():
    p = person(person_pygame_fake(None), 1281, 737, 25)
    result = p.check_screen_pos()
    assert p.posy == 736

def test_screen_posy_bounds_under():
    p = person(person_pygame_fake(None), 1281, 735, 25)
    result = p.check_screen_pos()
    assert p.posy == 735

class person_pygame_fake:
    def __init__(self, surface):
        self.person_shopping = None
        self.surface = surface

    def process_draw(self, posx, posy):
        pass

    def process_move(self, posx, posy):
        pass
