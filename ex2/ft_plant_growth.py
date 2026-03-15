#!/usr/bin/env python3
class Plant:
    def __init__(self, name: str, height: int, age: int):
        self.name = name
        self.height = height
        self.age = age

    def get_info(self):
        print(f"{self.name}: {self.height}cm, {self.age} days old")

    def grow(self):
        self.height += 6

    def age_plant(self):
        self.age += 6


Plants = [
    Plant("Rose", 25, 30),
    Plant("Sunflower", 80, 45),
    Plant("Cactus", 15, 120)
]


def ft_plant_growth():
    for i in Plants:
        print("=== Day 1 ===")
        i.get_info()
        for j in range(1, 8):
            if (j % 7 == 0):
                print(f"=== Day {j} ===")
                i.grow()
                i.age_plant()
                i.get_info()
                print("Growth this week: +6cm \n")


if __name__ == "__main__":
    ft_plant_growth()
