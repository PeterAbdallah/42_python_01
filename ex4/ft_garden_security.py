#!/usr/bin/env python3
class SecurePlant:
    def __init__(self, name: str, height: int, age: int):
        self.name = name
        self.__height = height
        self.__age = age
        print(f"Plant created: {self.name}")

    def get_height(self):
        return (self.__height)

    def get_age(self):
        return (self.__age)

    def set_height(self, height: int):
        if (height < 0):
            print(f"\nInvalid operation attempted: height \
{self.__height}cm [REJECTED]")
            print("Security: Negative height rejected")
        else:
            self.__height = height
            print(f"Height updated: {self.__height}cm [OK]")

    def set_age(self, age: int):
        if (age < 0):
            print(f"\nInvalid operation attempted: age \
{self.__age}days [REJECTED]")
            print("Security: Negative age rejected")
        else:
            self.__age = age
            print(f"Age updated: {self.__age} days [OK]")


def ft_garden_security():
    print("=== Garden Security System ===")
    rose = SecurePlant("Rose", 25, 30)
    rose.set_height(25)
    rose.set_age(30)
    rose.set_height(-5)
    print(f"\nCurrent plant: {rose.name} ({rose.get_height()}cm, \
{rose.get_age()} days)")


if __name__ == "__main__":
    ft_garden_security()
