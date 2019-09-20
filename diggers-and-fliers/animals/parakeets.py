from movements import IFlying
from movements import IWalking

class Parakeet(IFlying):
    def __init__(self, name):
        self.name = name
        IFlying.__init__(self, "45 mph")
        IWalking.__init__(self, "3 mph", 2)

    def flying(self):
        print(f"{self.name} is flying at {self.flight_speed}!")

    def walking(self):
        print(f"{self.name} is hopping around at {self.walk_speed}.")

    def __str__(self):
        return f'{self.name} the Parakeet'