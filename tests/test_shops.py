import pytest
from power.shops import shops

def test_get_shopum_firstrow():
    s = shops(shops_pygame_fake(None, '1_image'))
    s.draw_to_screen()
    assert s.shopnum == 1
    assert s.posx == 140
    assert s.posy == 50

def test_get_shopum_secondrow():
    s = shops(shops_pygame_fake(None, '5_image'))
    s.draw_to_screen()
    assert s.shopnum == 5
    assert s.posx == 140
    assert s.posy == 678
    
class shops_pygame_fake:

    def __init__(self, surface, image_uri):
        self.image_uri = image_uri
        self.surface = surface
        self.store_logo = None

    def draw_to_screen(self, posx, posy):
        pass