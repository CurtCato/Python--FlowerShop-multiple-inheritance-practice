from . import Habitat
from movements import IFlying

class Aviary(Habitat):

    def __init__(self, name):
        super().__init__(name)

    # Duck typing check
    # def add_flyer_pythonic(self, animal):
    #     try:
    #         if animal.flight_speed > -1:
    #             self.animals.add(animal)
    #     except AttributeError as ex:
    #         print(f'{animal} can\'t fly, so please do not try to put it in the {self.name} aviary.')

    # Actual typing check
    def add_flier_type_check(self, animal):
        if isinstance(animal, IFlying):
            self.animals.add(animal)
        else:
            print(f'{animal} can\'t fly, so please do not try to put it in the {self.name} aviary')