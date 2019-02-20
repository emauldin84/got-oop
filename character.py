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