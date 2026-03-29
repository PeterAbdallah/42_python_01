#!/usr/bin/env python3
class Plant:
    def __init__(self, name: str, height: float, age: int):
        self.name = name
        self.height = height
        self.age = age
        self.stats = self.Stats(self.name)

    def show(self):
        print(f"{self.name}: {self.height:.1f}cm, {self.age} days old")
        self.stats.addShow()

    def grow(self, growth: int):
        self.height += growth
        self.stats.addGrow()

    def age_plant(self, days: int):
        self.age += days
        self.stats.addAge()

    @staticmethod
    def is_older_than_year(age: int):
        print(f"Is {age} days more than a year? -> ", age > 365)

    @classmethod
    def create_anonymous(cls):
        anonymous = cls("Unknown plant", 0, 0)
        return (anonymous)

    class Stats():
        def __init__(self, name: str):
            self._name = name
            self._numOfgrow = 0
            self._numOfage = 0
            self._numOfshow = 0

        def addGrow(self):
            self._numOfgrow += 1

        def addAge(self):
            self._numOfage += 1

        def addShow(self):
            self._numOfshow += 1

        def show_stats(self):
            print(f"[statistics for {self._name}]")
            print(f"Stats: {self._numOfgrow} grow,\
 {self._numOfage} age, {self._numOfshow} show")


class Flower(Plant):
    def __init__(self, name: str, height: float, age: int, color: str):
        super().__init__(name, height, age)
        self.color = color
        self.blooming = False

    def bloom(self):
        self.blooming = True

    def show(self):
        super().show()
        print(f"Color: {self.color}")
        if (self.blooming):
            print(f"{self.name} is blooming beautifully!")
        else:
            print(f"{self.name} has not bloomed yet")


class Tree(Plant):
    def __init__(self, name: str, height: float, age: int,
                 trunk_diameter: int):
        super().__init__(name, height, age)
        self.trunk_diameter = trunk_diameter

    def produce_shade(self):
        print(f"Tree {self.name} now produces a shade of {self.height:.1f}cm\
 long and {self.trunk_diameter:.1f}cm wide.")
        self.stats.addShade()

    def show(self):
        super().show()
        print(f"Trunk diameter: {self.trunk_diameter:0.1f}cm")

    class Stats(Plant.Stats):
        def __init__(self, name: str):
            super().__init__(name)
            self._numOfshade = 0

        def addShade(self):
            self._numOfshade += 1

        def show_stats(self):
            super().show_stats()
            print(f"{self._numOfshade} shade")


class Vegetable(Plant):
    def __init__(self, name: str, height: float, age: int,
                 harvest_season: str, nutritional_value):
        super().__init__(name, height, age)
        self.harvest_season = harvest_season
        self.nutritional_value = nutritional_value

    def show(self):
        super().show()
        print(f"Harvest season: {self.harvest_season}")
        print(f"Nutritional value: {self.nutritional_value}")

    def grow(self, growth: int):
        super().grow(growth)


class Seed(Flower):
    def __init__(self, name: str, height: float, age: int, color: str):
        super().__init__(name, height, age, color)
        self.seeds = 0

    def show(self):
        super().show()
        print(f"Seeds: {self.seeds}")

    def age_plant(self, days):
        super().age_plant(days)
        self.seeds += 42


def ft_garden_analytics():
    print("=== Garden statistics ===")

    # Year check
    print("=== Check year-old")
    Plant.is_older_than_year(30)
    Plant.is_older_than_year(400)

    # Flower check
    print("\n=== Flower")
    Rose = Flower("Rose", 15, 10, "red")
    Rose.show()
    Rose.stats.show_stats()
    print("[asking the rose to grow and bloom]")
    Rose.grow(8)
    Rose.bloom()
    Rose.show()
    Rose.stats.show_stats()

    # Tree check
    print("\n=== Tree")
    Oak = Tree("Oak", 200, 365, 5)
    Oak.show()
    Oak.stats.show_stats()
    print("[asking the oak to produce shade]")
    Oak.produce_shade()
    Oak.stats.show_stats()

    # Seed check
    print("\n=== Seed")
    Sunflower = Seed("Sunflower", 80, 45, "yellow")
    Sunflower.show()
    print("[make sunflower grow, age and bloom]")
    Sunflower.age_plant(20)
    Sunflower.grow(30)
    Sunflower.bloom()
    Sunflower.show()
    Sunflower.stats.show_stats()

    # Anonymous check
    print("\n=== Anonymous")
    Anonymous = Plant.create_anonymous()
    Anonymous.show()
    Anonymous.stats.show_stats()


if __name__ == "__main__":
    ft_garden_analytics()
