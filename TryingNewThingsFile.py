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


class Cat(Animal):

    def say(self):
        return "Meow"


cat = Cat("Simon", 10)
first_animal = Animal("Alex", 10)
second_animal = Animal("Svenya", 10)
first_animal.change_color("red")
