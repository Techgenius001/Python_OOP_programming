# vehicles.py
# This file demonstrates polymorphism with a Vehicle base class and subclasses implementing move() differently

class Vehicle:
    """
    Base class for vehicles.
    """
    def move(self):
        """Base move method to be overridden by subclasses."""
        # This raises an error if subclasses do not implement their own move()
        raise NotImplementedError("Subclasses must implement this method.")

class Car(Vehicle):
    def move(self):
        print("Driving 🚗")  # Car-specific implementation of move()

class Plane(Vehicle):
    def move(self):
        print("Flying ✈️")  # Plane-specific implementation of move()

class Boat(Vehicle):
    def move(self):
        print("Sailing ⛵")  # Boat-specific implementation of move()

# Example usage (Uncomment to test)
# vehicles = [Car(), Plane(), Boat()]
# for v in vehicles:
#     v.move()  # Calls each class's move() method, demonstrating polymorphism
