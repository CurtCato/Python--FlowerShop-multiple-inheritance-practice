from . import Habitat
from movements import IDigging

class DirtPot(Habitat):

    def __init__(self, name):
        super().__init__(name)

    # Actual typing check
    def add_digger_type_check(self, animal):
        if isinstance(animal, IDigging):
            self.animals.add(animal)
        else:
            print(f'{animal} can\'t dig, so please do not try to put it in the {self.name} Dirt Pot')