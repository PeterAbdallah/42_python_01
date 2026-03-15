#!/usr/bin/env python3
class Plant:
    def __init__(self, name: str, height: int, age: int):
        self.name = name
        self.height = height
        self.age = age

    def get_info(self) -> str:
        print(f"{self.name}: {self.height}cm, {self.age} days old")


class Flower(Plant):
    def __init__(self, name: str, height: int, age: int, color: str):
        super().__init__(name, height, age)
        self.color = color

    def bloom(self):
        print("Flower is blooming beautifully!\n")

    def get_info(self) -> str:
        print(f"{self.name}(Flower): {self.height}cm, {self.age} days, \
{self.color} color")


class Tree(Plant):
    def __init__(self, name: str, height: int, age: int, trunk_diameter: int):
        super().__init__(name, height, age)
        self.trunk_diameter = trunk_diameter

    def produce_shade(self):
        print("Tree producing shade!\n")

    def get_info(self) -> str:
        print(f"{self.name}(Tree): {self.height}cm, {self.age} days, \
{self.trunk_diameter}cm diameter")


class Vegetable(Plant):
    def __init__(self, name: str, height: int, age: int,
                 harvest_season: str, nutritional_value):
        super().__init__(name, height, age)
        self.harvest_season = harvest_season
        self.nutritional_value = nutritional_value

    def get_info(self) -> str:
        print(f"{self.name}(Tree): {self.height}cm, {self.age} days, \
{self.harvest_season} harvest\n{self.nutritional_value}")


def ft_plant_types():
    rose = Flower("Rose", 25, 30, "red")
    oak = Tree("Oak", 500, 1825, 50)
    tomato = Vegetable("Tomato", 120, 60, "Summer", "Rich in vitamin C")
    print("=== Garden Plant Types ===\n")
    rose.get_info()
    rose.bloom()
    oak.get_info()
    oak.produce_shade()
    tomato.get_info()


if __name__ == "__main__":
    ft_plant_types()
