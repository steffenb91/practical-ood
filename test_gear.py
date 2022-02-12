
from Gear import Gear

def test_gear():
    gear = Gear(52, 11, 26, 1.5)
    assert gear.gear_inches() == 137.0909090909091 