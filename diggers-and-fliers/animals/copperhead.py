from movements import ISwimming
from movements import IWalking

class Copperhead(ISwimming, IWalking):
    def __init__(self, name):
        self.name = name
        ISwimming.__init__(self, "12 mph", "20 ft")
        IWalking.__init__(self, "9 mph", 0)

    def slithering(self):
        print(f"{self.name} the copperhead is slithering around at {self.walk_speed}.")

    def swimming(self):
        print(f"{self.name} is swimming around the river at {self.swim_speed}.")

    def __str__(self):
        return f'{self.name} the Copperhead'