#!/usr/bin/env python3

class Plant:
    def __init__(self, name: str, height: int, age: int):
        self.name = name
        self.height = height
        self.age = age

    def show(self):
        print(f"{self.name}: {self.height}cm, {self.age} days old")


Plants = [
    Plant("Rose", 25, 30),
    Plant("Sunflower", 80, 45),
    Plant("Cactus", 15, 120)
]


def ft_garden_data():
    print("=== Garden Plant Registry ===")
    for i in Plants:
        i.show()


if __name__ == "__main__":
    ft_garden_data()
