# Parent class
class Vehicle:
    def move(self):
        pass  # This will be overridden by child classes

# Child classes
class Car(Vehicle):
    def move(self):
        return "Driving 🚗"

class Plane(Vehicle):
    def move(self):
        return "Flying ✈️"

class Boat(Vehicle):
    def move(self):
        return "Sailing 🚤"

# Create a list of vehicles
vehicles = [Car(), Plane(), Boat()]

# Polymorphism in action
for v in vehicles:
    print(v.move())
