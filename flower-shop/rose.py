from flowers import Flowers
from inorganic import Inorganic

class Roses(Flowers, Inorganic):
    def __init__(self, color):
        Flowers.__init__(self, 7, color)
        Inorganic.__init__(self)

