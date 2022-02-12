from Weel import Weel

class Gear:

    def __init__(self, chainring, cog, rim, tire) -> None:
        self.chainring = chainring
        self.cog=cog
        self.rim=rim
        self.tire=tire

    def gear_inches(self):
        return self.ratio() * Weel(self.rim, self.tire).diameter()
    
    def ratio(self):
        return self.chainring / self.cog