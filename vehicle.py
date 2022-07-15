class Car():
    """Creating car with attributes"""
    def __init__(self, model, year, engine_cap, price, mileage):
        self.model = model
        self.year = year
        self.engine_cap = engine_cap
        self.price = price
        self.mileage = mileage
        self.num_wheels = 4

    def vehicle_description(self):
        """Getting description of the vehicle"""
        print("Model of vehicle: " + str(self.model) + "\nYear of production: " + str(self.year) + "\nEngine Capacity: "
              + str(self.engine_cap) + "\nMileage: " + str(self.mileage) + "\nNumber of wheels: "
              + str(self.num_wheels) + "\nPrice: " + str(self.price))


class Truck(Car):
    """Initializing successor from class Car"""
    def __init__(self, model, year, engine_cap, price, mileage):
        super().__init__(model, year, engine_cap, price, mileage)
        self.num_wheels = 8


vehicle_car = Car("Ford", 2010, 1.6, "$3500", 95000)
vehicle_car.vehicle_description()

vehicle_truck = Truck("Volvo", 2019, 16, "$33300", 220000)
vehicle_truck.vehicle_description()