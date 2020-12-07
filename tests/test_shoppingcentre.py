import pytest
from power.shopping_centre import shopping_centre
from power.power import power

def test_is_power_returned():
    sc = shopping_centre(10)
    sc.displayobj = shopping_centre_pygame_fake(100, 100)
    assert len(sc.init_power_text()) == 3
    assert type(sc.init_power_text()[0]) is power

def test_draw_shops_count_logos():
    sc = shopping_centre(10)
    sc.displayobj = shopping_centre_pygame_fake(100, 100)
    sc.draw_shops()
    assert len(sc.all_shops) == 8
    
class shopping_centre_pygame_fake:

    def __init__(self, width, height):
        self.width = width 
        self.height = height

    def init_power_text(self):
        # initiate the font loader
        return None, None

    def build_display_caption(self):
        return None

    def draw_internal_shops_1(self):
        pass

    def draw_internal_shops_2(self, logo):
        return logo