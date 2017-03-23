class Person():
    def __init__(self, name, age):
        self.name = name
        self.age = age if age else 0

    def is_major(self):
        return True if self.age >= 18 else False
