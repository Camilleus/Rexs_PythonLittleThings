class Animal:
    color = "white"

    def __init__(self, nickname, weight):
        self.nickname = nickname
        self.weight = weight

    def say(self):
        pass

    def change_weight(self, weight):
        self.weight = weight

    def change_color(self, new_color):
        Animal.color = new_color


class Owner:
    def __init__(self, name, age, address):
        self.name = name
        self.age = age
        self.address = address

    def info(self):
        return {
            "name": self.name,
            "age": self.age,
            "address": self.address
        }


class Cat(Animal):

    def say(self):
        return "Meow"


class Dog(Animal):
    def __init__(self, nickname, weight, breed):
        super().__init__(nickname, weight)
        self.breed = breed

    def say(self):
        return "Woof"


dog = Dog("Barbos", 23, "labrador")
cat = Cat("Simon", 10)
first_animal = Animal("Alex", 10)
second_animal = Animal("Svenya", 10)
first_animal.change_color("red")
