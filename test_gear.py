
from gear import Gear
from wheel import Wheel

def test_gear():
    wheel = Wheel(26, 1.5)
    gear = Gear(52, 11, wheel)
    assert gear.gear_inches() == 137.0909090909091