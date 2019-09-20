from movements import IWalking, ISwimming

class Penguin(IWalking, ISwimming):

    def __init__(self, name):
        ISwimming.__init__(self, "10 mph", "30 ft")
        IWalking.__init__(self, "2 mph", 2)
        self.name = name

    def run(self):
        print(f'{self.name} waddles with {self.legs} legs')

    def __str__(self):
        return f'{self.name} the Penguin'