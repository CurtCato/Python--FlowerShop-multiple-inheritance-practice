
class Arrangement:

    def __init__(self):
        self.__flowers = []

    def enhance(self, flower):
        try:
            if flower.organic == False:
                self.__flowers.append(flower)
        except AttributeError:
            print(f"Inorganic flowers only")

    def add_organic_flower(self, flower):
        try:
            if flower.organic == True:
                self.__flowers.append(flower)
        except AttributeError:
            print(f"Organic flowers only")