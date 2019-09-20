from flowers import Flowers
from inorganic import Inorganic

class Alstroemeria(Flowers, Inorganic):
    def __init__(self):
        Flowers.__init__(self, 7, "purple")
        Inorganic.__init__(self)