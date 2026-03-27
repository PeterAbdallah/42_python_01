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


def ft_plant_growth():
    Rose = Plant("Rose", 25, 30)
    weekly_growth = 0
    print("=== Garden Plant Growth ===")
    for i in range(1, 8):
        print(f"=== Day {i} ===")
        Rose.show()
        if (i != 7):
            Rose.grow(0.8)
            weekly_growth += 0.8
            Rose.age_plant(1)
    print(f"Growth this week: {weekly_growth}cm")


if __name__ == "__main__":
    ft_plant_growth()
