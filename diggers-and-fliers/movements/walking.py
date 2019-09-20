class IWalking:

    def __init__(self, WS, legs):
        self.walk_speed = WS
        self.legs = legs

    def run(self):
        print(f"{self.name} walks at {self.walk_speed}")