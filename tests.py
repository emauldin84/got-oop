# these aren't real tests

from character import Character
from character import Hero
from character import Monster

# Characters can be instantiated with name and avatar

arya = Character("Arya Stark", "arya.png")
jon = Character("Jon Snow", "jon.png")

print(arya.name, arya.avatar)
print(jon.name, jon.avatar)

# After two items to inventory, length of inventory should == 2

arya.inventory.append('Needle')
arya.inventory.append('mask')

print("Arya has %d items in her inventory" % len(arya.inventory))

# Arya should have a `greet` method 
# and when I call it with `arya.greet(jon)`, it should return ""Hello, Jon Snow. I am Arya Stark. I am awesome""

print(arya.greet(jon))

# Arya should have a `greet` method 
# and when I call it with `arya.greet()`, it should return ""Hello. I am Arya Stark. I am awesome""

print(arya.greet())


# I should be able to create a `Hero` instance
bronn = Hero("Bronn of the Blackwater", "bron.png")

# Hero should be able to .greet a Character
print(bronn.greet(arya))
print(jon.greet(bronn))


# I should be able to create  `Monster` instance
night_king = Monster("Night King", "night_king.png")

# Monster should be able to .greet a Character
print(bronn.greet(night_king))
print(night_king.greet(arya))

print(night_king.monster_greet(jon))

# Expect Jon to say "EEEEEEEEEK!"
# when encountering a monster
print(bronn.greet(night_king))
