from animals import Penguin, PaintedDog, Copperhead, BettaFish, Parakeet, Earthworm
from habitats import Aquarium, Aviary, Terrestrial, DirtPot

waddles = Penguin("Waddles")
doggy = PaintedDog("Doggy")
wormy = Earthworm("Wormy")
wingsy = Parakeet("Wingsy")
snakey = Copperhead("Snakey")
fishy = BettaFish("Fishy")

wormy.digging()
snakey.slithering()
fishy.swim()
doggy.run()
waddles.run()
waddles.swim()
wingsy.flying()

print(wingsy.__dict__)
print(wormy.__dict__)

seaworld = Aquarium("Sea World")
seaworld.add_swimmer_type_check(waddles)
seaworld.add_swimmer_type_check(fishy)
seaworld.add_swimmer_type_check(snakey)

skyworld = Aviary("Sky World")
skyworld.add_flier_type_check(wingsy)

landworld = Terrestrial("Land World")
landworld.add_walking_type_check(snakey)
landworld.add_walking_type_check(doggy)
landworld.add_walking_type_check(waddles)
landworld.add_walking_type_check(wormy)

dirtpot = DirtPot("Dirt Pot")
dirtpot.add_digger_type_check(wormy)

for animal in seaworld.animals:
    print(f'{animal} lives in Sea World')

for animal in skyworld.animals:
    print(f"{animal} lives in Sky World")

for animal in landworld.animals:
    print(f"{animal} lives in Land World")

for animal in dirtpot.animals:
    print(f"{animal} lives in a Dirt Pot")

