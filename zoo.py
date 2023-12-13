class Animal:
  def __init__(self, name, color):
    self.name = name
    self.color = color

  def eat(self):
    print(f'{self.name} is eating.')

  def sleep(self):
    print(f'{self.name} is sleeping.')

  def make_sound(self):
    print(f'{self.name} is making a sound.')

class Dog(Animal):
  def __init__(self, name, color, breed):
    super().__init__(name, color)
    self.breed = breed

  def bark(self):
    print(f'{self.name} is barking.')

class Cat(Animal):
  def __init__(self, name, color, age):
    super().__init__(name, color)
    self.age = age

  def meow(self):
    print(f'{self.name} is meowing.')

# Create an instance of the Dog class
dog = Dog('Max', 'brown', 'Labrador')

# Call the eat(), sleep(), make_sound(), and bark() methods on the dog object
dog.eat()
dog.sleep()
dog.make_sound()
dog.bark()

# Create an instance of the Cat class
cat = Cat('Kitty', 'white', 3)

# Call the eat(), sleep(), make_sound(), and meow() methods on the cat object
cat.eat()
cat.sleep()
cat.make_sound()
cat.meow()
