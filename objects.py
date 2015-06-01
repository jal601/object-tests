""" Objects models file.

    Edit the class definitions to make the tests pass.
"""


class Dessert(object):

    # Edit me!
    # You need to be able to initialize a Dessert object with arguments:
    # price - required
    # calories - optional

    # This should set the object's price and calories, accessible by
    # .price and .calories respectively.

    def __init__(self, price, calories=None):
        self.price = price
        self.calories = calories

    # Add a calories_per_dollar method that returns the calories per dollar
    # for the dessert.

    def calories_per_dollar(self):
        if self.calories == None:
            return None
        else:
            return self.calories / self.price

    # Define a method is_a_cake on Dessert that returns False

    def is_a_cake(self):
        return False


class Cake(Dessert):

    # Edit me!
    # Cakes all cost the same amount and have the same calories, so their
    # price and calories can be set at the class-level, not during init.
    
    price = 5
    calories = 200

    # However, we need to be able to tell cakes apart. Accept arguemtn:
    # kind - required

    def __init__(self, kind):
        self.kind = kind

    # Define a method is_a_cake on Cake that returns True
    # (This will override the one on Dessert)

    def is_a_cake(self):
        return True


class Menu(object):

    def __init__(self, items):
        self.items = items

    def desserts(self):
        # Return only the items in self.items which are desserts
        desserts = []
        for item in self.items:
            if isinstance(item, Dessert):
                desserts.append(item)
        return desserts

    def cakes(self):
        # Return only the items in self.items which are cakes
        cakes = []
        for item in self.items:
            if isinstance(item, Cake):
                cakes.append(item)
        return cakes

