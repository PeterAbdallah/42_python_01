#!/usr/bin/env python3
class Plant:
    def __init__(self, name: str, height: int, age: int):
        self.name = name
        self.height = height
        self.age = age

    def show(self) -> str:
        return (f"{self.name}: {self.height:.1f}cm, {self.age} days old")


def ft_plant_factory():
    plant_data = [
        ("Rose", 25, 30),
        ("Oak", 200, 365),
        ("Cactus", 5, 90),
        ("Sunflower", 80, 45),
        ("Fern", 15, 120)
    ]
    plants = []
    for plant in plant_data:
        # plants.append(Plant(plant[0], plant[1], plant[2]))
        plants.append(Plant(*plant))
    print("=== Plant Factory Output ===")
    for i in plants:
        print(f"Created: {i.show()}")


if __name__ == "__main__":
    ft_plant_factory()
