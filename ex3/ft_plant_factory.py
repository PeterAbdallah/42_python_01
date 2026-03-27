#!/usr/bin/env python3
class Plant:
    def __init__(self, name: str, height: int, age: int):
        self.name = name
        self.height = height
        self.age = age

    def show(self) -> str:
        return (f"{self.name}: {self.height:.1f}cm, {self.age} days old")


plant_data = [
    ("Rose", 25, 30),
    ("Oak", 200, 365),
    ("Cactus", 15, 120),
    ("Sunflower", 80, 45),
    ("Fern", 15, 120)
]


def ft_plant_factory():
    # plant_data.append(("zebra", 20, 60))
    Plants = []
    for data in plant_data:
        Plants.append(Plant(data[0], data[1], data[2]))
        # Plants.append(Plant(*data))
    print("=== Plant Factory Output ===")
    for i in Plants:
        print("Created: ", i.show())


if __name__ == "__main__":
    ft_plant_factory()
