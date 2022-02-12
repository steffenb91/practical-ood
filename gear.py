from wheel import Wheel

class Gear:

    def __init__(self, chainring, cog, wheel) -> None:
        self.chainring = chainring
        self.cog = cog
        self.wheel = wheel

    def gear_inches(self):
        return self.ratio() * self.wheel.diameter()
    
    def ratio(self):
        return self.chainring / self.cog