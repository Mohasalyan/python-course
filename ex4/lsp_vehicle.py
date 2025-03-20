# Liskov Substitution Principle (LSP)

class Vehicle:
    """
    Base Vehicle class.
    """
    def start(self) -> None:
        raise NotImplementedError


class EngineVehicle(Vehicle):
    """
    Vehicles that have an engine.
    """
    def start(self) -> None:
        print("Engine started!")


class NonEngineVehicle(Vehicle):
    """
    Vehicles without an engine.
    """
    def start(self) -> None:
        print("This vehicle does not have an engine!")


# Concrete Implementations
class Car(EngineVehicle):
    pass


class Bicycle(NonEngineVehicle):
    pass


# Example Usage
car = Car()
bike = Bicycle()

car.start()  # "Engine started!"
bike.start()  # "This vehicle does not have an engine!"
