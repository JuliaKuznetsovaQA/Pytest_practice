class Car():
    def __init__(self, model, year, engine_vol, price, dist):
        self.model = model
        self.year = year
        self.engine_vol = engine_vol
        self.price = price
        self.dist = dist
        self.wheels = 4

    def description_car(self):
        """Описание машины"""
        description = self.model + " " + str(self.year) + " года выпуска, объем двигателя " + str(self.engine_vol) + ", цена " + str(self.price) + " $, пробег " + str(self.dist) + ", количество колес: " + str(self.wheels)
        print(description)

car = Car("Toyota", 2020, 3, 10000, 12000)
car.description_car()

class Lorry(Car):
    def __init__(self, model, year, engine_vol, price, dist):
        super().__init__(model, year, engine_vol, price, dist)
        self.wheels = 8

lorry = Lorry("КАМАЗ", 2018, 8, 40000, 100000)
lorry.description_car()