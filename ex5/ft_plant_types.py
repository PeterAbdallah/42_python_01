#!/usr/bin/env python3
class Plant:
    def __init__(self, name: str, height: int, age: int):
        self.name = name
        self.height = height
        self.age = age

    def show(self):
        print(f"{self.name}: {self.height:.1f}cm, {self.age} days old")

    def grow(self, growth: int):
        self.height += growth

    def age_plant(self, days: int):
        self.age += days


class Flower(Plant):
    def __init__(self, name: str, height: int, age: int, color: str):
        super().__init__(name, height, age)
        self.color = color

    def bloom(self):
        print(f"{self.name} has not bloomed yet")
        print(f"[asking the {self.name} to bloom]")
        self.show()
        print(f"{self.name} is blooming beautifully!\n")

    def show(self):
        super().show()
        print(f"Color: {self.color}")


class Tree(Plant):
    def __init__(self, name: str, height: int, age: int, trunk_diameter: int):
        super().__init__(name, height, age)
        self.trunk_diameter = trunk_diameter

    def produce_shade(self):
        print(f"[asking the {self.name} to produce shade]")
        print(f"Tree {self.name} now produces a shade of {self.height:.1f}cm\
 long and {self.trunk_diameter:.1f}cm wide.\n")

    def show(self):
        super().show()
        print(f"Trunk diameter: {self.trunk_diameter:0.1f}cm")


class Vegetable(Plant):
    def __init__(self, name: str, height: int, age: int,
                 harvest_season: str, nutritional_value):
        super().__init__(name, height, age)
        self.harvest_season = harvest_season
        self.nutritional_value = nutritional_value

    def show(self):
        super().show()
        print(f"Harvest season: {self.harvest_season}")
        print(f"Nutritional value: {self.nutritional_value}")

    def grow(self, growth: int, age: int):
        super().grow(growth)
        super().age_plant(age)
        print(f"[make {self.name} grow and age for {age} days]")
        self.nutritional_value += age


def ft_plant_types():
    rose = Flower("Rose", 15, 10, "red")
    oak = Tree("Oak", 200, 365, 5)
    tomato = Vegetable("Tomato", 5, 10, "April", 0)
    print("=== Garden Plant Types ===")
    print("=== Flower")
    rose.show()
    rose.bloom()
    print("\n=== Tree")
    oak.show()
    oak.produce_shade()
    print("\n=== Vegetable")
    tomato.show()
    tomato.grow(42, 20)
    tomato.show()


if __name__ == "__main__":
    ft_plant_types()
