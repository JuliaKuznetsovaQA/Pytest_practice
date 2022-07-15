class Person():
    """Модель человека"""

    def __init__(self, name, age):
        """Инициализация атрибутов человека - имя, возраст"""
        self.name = name
        self.age = age
        print("Человек создан")

    def sing(self):
        """Просим человека спеть"""
        print(self.name + " поет")

    def dance(self):
        """Просим человека станцевать"""
        print(self.name + " танцует")

man = Person("Андрей", 16)
woman = Person("Настя", 30)


woman.sing()
man.dance()

