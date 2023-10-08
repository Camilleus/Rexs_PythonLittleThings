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
    def __init__(self, nickname, weight, breed, owner):
        self.breed = breed
        self.owner = owner
        super().__init__(nickname, weight)

    def say(self):
        return "Woof"

    def who_is_owner(self):
        return self.owner.info()


class CatDog(Cat, Dog):
    def say(self):
        return "Meow"

    def info(self):
        return f"{self.nickname}-{self.weight}"


class DogCat(Dog, Cat):
    def say(self):
        return "Woof"

    def info(self):
        return f"{self.nickname}-{self.weight}"


dog = Dog("Barbos", 23, "labrador")
cat = Cat("Simon", 10)
first_animal = Animal("Alex", 10)
second_animal = Animal("Svenya", 10)
first_animal.change_color("red")
