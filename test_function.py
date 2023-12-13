class Animal:
    def __init__(self, name, sound):
        self.name = name
        self.sound = sound

    def make_sound(self):
        print(f"{self.name} says {self.sound}")

    #Creating the objects

cat= Animal("Cat","Meow")
dog= Animal("Dog","Woof")
Elephant= Animal ("Elephant","Trumpet")

cat.make_sound()
dog.make_sound()


