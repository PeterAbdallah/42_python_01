#!/usr/bin/env python3
class SecurePlant:
    def __init__(self, name: str, height: int, age: int):
        self.name = name
        self._height = height
        self._age = age
        print(f"Plant created: {self.show()}")

    def show(self) -> str:
        return (f"{self.name}: {self._height:.1f}cm, {self._age}\
 days old")

    def get_height(self):
        return (self._height)

    def get_age(self):
        return (self._age)

    def set_height(self, height: int):
        if (height < 0):
            print(f"\n{self.name}: Error, height can't be negative")
            print("Height update rejected")
        else:
            self._height = height
            print(f"\nHeight updated: {self._height}cm")

    def set_age(self, age: int):
        if (age < 0):
            print(f"\n{self.name}: Error, age can't be negative")
            print("Age update rejected")
        else:
            self._age = age
            print(f"Age updated: {self._age} days")


def ft_garden_security():
    print("=== Garden Security System ===")
    rose = SecurePlant("Rose", 15, 10)
    rose.set_height(25)
    rose.set_age(30)
    rose.set_height(-5)
    rose.set_age(-5)
    print(f"\nCurrent state: {rose.name}: {rose.get_height():.1f}cm, \
{rose.get_age()} days old")


if __name__ == "__main__":
    ft_garden_security()
