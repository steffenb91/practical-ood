
from gear import Gear
from wheel import Wheel

def test_gear():
    gear = Gear(chainring = 52, cog = 11, wheel = Wheel(26, 1.5))
    assert gear.gear_inches() == 137.0909090909091