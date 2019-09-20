from movements import ISwimming

class BettaFish(ISwimming):
    def __init__(self, name):
        self.name = name
        ISwimming.__init__(self, "15 mph", "80 ft")

    def swim(self):
        print(f"{self.name} is swimming at {self.swim_speed}.")

    def __str__(self):
        return f'{self.name} the BettaFish'
