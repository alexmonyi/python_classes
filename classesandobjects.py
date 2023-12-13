class Things:
    pass
class Inanimate(Things):
    pass
class Animate(Things):
    pass
class Sidewalks(Inanimate):
    pass
class Animals(Animate):
    def breathe(self):
     pass
    def move(self):
     pass
    def eat_food(self):
     pass
class Mammals(Animals):
    pass
class Girraffes(Mammals):
    pass
Jeremy=Girraffes()

Jeremy.move()
