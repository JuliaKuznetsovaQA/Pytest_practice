from base_person import Person

class Warrior(Person):
    """Создаем класс воина"""

    def __init__(self, name, age, height):
        """Инициализируем атрибуты класса родителя"""
        super().__init__(name, age, height)
        self.rage = 100


    def get_rage(self):
        """Получение заряда ярости"""
        print("Заряд ярости равен: " + str(self.rage))


    def description_person(self):
        """Переопределение метода родителя"""
        description = self.name + ", ему " + str(self.age) + ", его заряд ярости " + str(self.rage)
        # print("Нового воина зовут " + description)
        return description


warrior = Warrior("Конан", 32, 200)
print("Нового воина зовут " + warrior.description_person())