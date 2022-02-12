class Weel:

    def __init__(self, rim, tire) -> None:
        self.rim = rim
        self.tire = tire

    def diameter(self):
        return self.rim + (self.tire * 2)