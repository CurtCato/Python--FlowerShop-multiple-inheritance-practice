from alstroemeria import Alstroemeria
from baby import BabyBreath
from daisies import Daisies
from lillies import Lillies
from poppies import Poppies
from rose import Roses
from arrangements import Arrangement
from valentines import ValentinesDay
from mothers import MothersDay

valentines_day_arrangement = ValentinesDay()
mothers_day_arrangement = MothersDay()

alstro = Alstroemeria()
lilly = Lillies()
red_rose = Roses("red")
white_rose = Roses("white")
purple_rose = Roses("purple")

daisy = Daisies()
poppy = Poppies()
baby = BabyBreath()

valentines_day_arrangement.add_organic_flower(daisy)
valentines_day_arrangement.add_organic_flower(poppy)
valentines_day_arrangement.add_organic_flower(baby)

mothers_day_arrangement.enhance(alstro)
mothers_day_arrangement.enhance(lilly)
mothers_day_arrangement.enhance(red_rose)
mothers_day_arrangement.enhance(white_rose)
mothers_day_arrangement.enhance(purple_rose)


print(valentines_day_arrangement._Arrangement__flowers)



    # Override the `enhance` method to ensure only
    # roses, lillies, and alstroemeria can be added





# class Rose:
#     pass

# if __name__ == "__main__":
#     for_beth = ValentinesDay()
#     red_rose = Rose()

#     for_beth.flowers.append(red_rose)


# Mother's Day Arrangement
# The Mother's Day arrangement contains daisies, baby's breath, and poppies.
# This arrangement is a bit more reserved, and Jake makes sure that each flower stem is cut to 4 inches.

# Also, each flower in this arrangement is organically grown with no pesticides used.
# Because of this, these arrangements have to be transported in a non-refrigerated container.

# Valentine's Day Arrangement
# The Valentine's Day arrangement includes the traditional rose. Jake has red, pink, and blue ones to
# send the right message. It also has lillies and alstroemeria to add more depth to the color of the arrangement.

# This arrangment is flamboyant and extravagent. Each flower stem is cut to 7 inches. Flowers in this arrangement
# are not organically grown, so they can be transported in a refrigerated container.