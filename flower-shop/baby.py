from flowers import Flowers
from organic import Organic

class BabyBreath(Flowers, Organic):
    def __init__(self):
        Flowers.__init__(self, 4, "pink")
        Organic.__init__(self)