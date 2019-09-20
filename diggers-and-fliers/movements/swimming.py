class ISwimming:

    def __init__(self, SS, MD):
        self.swim_speed = SS
        self.maximum_depth = MD

    def swim(self):
        print(f"{self.name} swims {self.maximum_depth} deep at {self.swim_speed}")