from movements import IDigging

class Earthworm(IDigging):
    def __init__(self, name):
        self.name = name
        IDigging.__init__(self, "0.5 mph")

    def digging(self):
        print(f"{self.name} is digging its way.")

    def __str__(self):
        return f'{self.name} the Earthworm'