from flowers import Flowers
from inorganic import Inorganic

class Lillies(Flowers, Inorganic):
    def __init__(self):
        Flowers.__init__(self, 7, "yellow")
        Inorganic.__init__(self)
