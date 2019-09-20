from . import Habitat
from movements import IWalking

class Terrestrial(Habitat):

    def __init__(self, name):
        super().__init__(name)

    # Actual typing check
    def add_walking_type_check(self, animal):
        if isinstance(animal, IWalking):
            self.animals.add(animal)
        else:
            print(f'{animal} can\'t walk, so please do not try to put it in the {self.name} walking path')