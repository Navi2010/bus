class Vehicle:
    def __init__(self, name, max_speed, mileage):
        self.name = name
        self.max_speed = max_speed
        self.mileage = mileage

    def display_info(self):
        print('vehicle name: ', self.name, 'max speed: ', self.max_speed, 'mph: ', self.mileage)

class Bus(Vehicle):
    def __init__(self, name, max_speed, mileage, capacity):
        super().__init__(name, max_speed, mileage)
        self.capacity = capacity

    def fare(self):
        fare = self.capacity * 10 #each person pays 10 bucks
        return fare
    
school_bus = Bus('school bus', 80, 12, 50)
school_bus.display_info()
print('total fare: $'+ str(school_bus.fare()))