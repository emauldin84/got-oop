# name
# avatar: (profile picture)
# inventory


class Character():
    def __init__(self, new_name, new_avatar): #the "dunder" __init__ method is the constructor
        # `self` is teh customary way to refer to the instance being built
        # in some other languages, they use `this`
        self.name = new_name
        self.avatar = new_avatar
        self.inventory = []
    
    # `someone=None` is a default argument
    # `None` is equal to `null` in other languages
    def greet(self, someone=None):
        # When we assume that `someone` argument has a `.name` property
        # this is an Object-Oriented programming principle called 
        # polymorphism
        # In Python, it's called "Duck Typing"
        if someone:
            return "Hello, %s. I am %s. I am awesome." % (someone.name, self.name,)
        else:
            return "Hello. I am %s. I am awesome." % (self.name,)


# `Hero` is a kind of `Character`
# `Hero` is a subclass of `Character`
# `Hero` inherits from `Character`
# `Character` is the super class of `Hero`
class Hero(Character):
    pass