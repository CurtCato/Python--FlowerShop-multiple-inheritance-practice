from movements import IWalking

class PaintedDog(IWalking):

    def __init__(self, name):
        self.name = name
        IWalking.__init__(self, "20 mph", 4)

    def __str__(self):
        return f'{self.name} the Painted Dog'