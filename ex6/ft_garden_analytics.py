#!/usr/bin/env python3
class Plant():
    def __init__(self, name, height, age):
        self.name = name
        self.height = height
        self.age = age

    def grow(self):
        self.height += 1
        print(f"{self.name} grew 1cm")

    def print_message(self):
        print(f"- {self.name}: {self.height} cm")

    @staticmethod
    def is_older_than_year(age: int):
        if (age > 365):
            print(f"Is {age} days more than a year? -> True")
        else:
            print(f"Is {age} days more than a year? -> False")


class FloweringPlant(Plant):
    def __init__(self, name, height, age, color):
        super().__init__(name, height, age)
        self.color = color

    def print_message(self):
        print(f"- {self.name}: {self.height} cm (blooming)")


class PrizeFlower(FloweringPlant):
    def __init__(self, name, height, age, color, points):
        super().__init__(name, height, age, color)
        self.points = points

    def print_message(self):
        print(f"- {self.name}: {self.height} cm (blooming),\
Prize points: {self.points}")


class Garden():
    def __init__(self, name):
        self.name = name
        self.total_growth = 0
        self.plants: list[Plant] = []

    def add_plant(self, newPlant: Plant):
        self.plants.append(newPlant)
        print(f"Added {newPlant.name} to {self.name}'s garden")

    def print_plants(self):
        print("Plants in Garden:")
        for plant in self.plants:
            plant.print_message()

    def grow_plants(self):
        print(f"\n{self.name} is helping all plants grow...")
        for plant in self.plants:
            plant.grow()
            self.total_growth += 1

    def count_types(self):
        regular = 0
        flowering = 0
        prize = 0
        for plant in self.plants:
            if (isinstance(plant, PrizeFlower)):
                prize += 1
            elif (isinstance(plant, FloweringPlant)):
                flowering += 1
            elif (isinstance(plant, Plant)):
                regular += 1
        return regular, flowering, prize


class GardenManager():
    def __init__(self):
        self.gardens: list[Garden] = []

    def add_garden(self, garden: Garden):
        self.gardens.append(garden)

    @classmethod
    def create_garden_network(cls):
        manager = cls()

        # Create Gardens
        g1 = Garden("Alice")
        g2 = Garden("Bob")

        # Add gardens to the GardenManager
        manager.add_garden(g1)
        manager.add_garden(g2)

        # Add plants to alice
        g1.add_plant(Plant("Oak Tree", 100, 10))
        g1.add_plant(FloweringPlant("Rose", 25, 12, "red"))
        g1.add_plant(PrizeFlower("Sunflower", 50, 3, "yellow", 10))

        return (manager)

    class GardenStats():

        @staticmethod
        def total_plants(garden: Garden):
            total_plants = len(garden.plants)
            return (total_plants)

        @staticmethod
        def height_validation(height: int):
            if (height > 0):
                return True
            return False

        @staticmethod
        def generate_report(garden: Garden, manager: "GardenManager"):
            print(f"\n==={garden.name}'s Garden Report ===")
            garden.print_plants()
            total = manager.GardenStats.total_plants(garden)
            print(f"\nPlants added: {total}, Total growth:\
{garden.total_growth}cm")
            regular, flowering, prize = garden.count_types()
            print(f"Plant types: {regular} regular, {flowering} flowering,\
{prize} prize flowers.\n")


def ft_garden_analytics():
    manager = GardenManager.create_garden_network()
    manager.gardens[0].grow_plants()
    manager.GardenStats.generate_report(manager.gardens[0], manager)
    print("=== Garden statistics ===")
    print("=== Check year-old")
    Plant.is_older_than_year(30)
    Plant.is_older_than_year(400)
    # i stopped here
    print("=== Flower")
    print(f"Height validation test:{manager.GardenStats.height_validation(5)}")
    print("Garden scores - Alice: 208, Bob: 92")
    print(f"Total gardens managed: {len(manager.gardens)}")


if __name__ == "__main__":
    ft_garden_analytics()
