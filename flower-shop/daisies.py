from flowers import Flowers
from organic import Organic

class Daisies(Flowers, Organic):
    def __init__(self):
        Flowers.__init__(self, 4, "white")
        Organic.__init__(self)