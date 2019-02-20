# these aren't real tests

from character import Character

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
# and when I call it, it should return "Hello. I am Arya Stark. I am awesome."

print(arya.greet())