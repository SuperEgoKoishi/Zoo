class Animal():
    """
    实现动物类
    """

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def walk(self):
        pass

    def run(self):
        pass

    def make_noise(self):
        pass


class Cat(Animal):
    """
    实现猫类,继承动物类
    """

    def __init__(self, name, age):
        super().__init__(name, age)

    def walk(self):
        print("cat walks")

    def run(self):
        print("cat runs")

    def make_noise(self):
        print("cat makes noise")


class Dog(Animal):
    """
    实现狗类,继承动物类
    """

    def __init__(self, name, age):
        super().__init__(name, age)

    def walk(self):
        print("dog walks")

    def run(self):
        print("dog runs")

    def make_noise(self):
        print("dog makes noise")


class Bird(Animal):
    """
    实现鸟类,继承动物类
    """

    def __init__(self, name, age):
        super().__init__(name, age)

    def walk(self):
        print("bird walks")

    def run(self):
        print("bird runs")

    def make_noise(self):
        print("bird makes noise")


if __name__ == '__main__':
    animal = [Cat("cat1", 1), Dog("dog1", 1), Bird("bird1", 1)]
    for i in range(3):
        animal[i].run()
