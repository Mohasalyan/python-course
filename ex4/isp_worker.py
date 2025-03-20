# Interface Segregation Principle (ISP)

from abc import ABC, abstractmethod


class Builder(ABC):
    @abstractmethod
    def build_construction(self) -> None:
        pass


class Waiter(ABC):
    @abstractmethod
    def serve_the_table(self) -> None:
        pass


class Teacher(ABC):
    @abstractmethod
    def check_hometask(self) -> None:
        pass


# Implementing Specific Roles
class ConcreteBuilder(Builder):
    def build_construction(self) -> None:
        print("Building a house!")


class ConcreteWaiter(Waiter):
    def serve_the_table(self) -> None:
        print("Serving food!")


class ConcreteTeacher(Teacher):
    def check_hometask(self) -> None:
        print("Checking homework!")


# Example Usage
builder = ConcreteBuilder()
waiter = ConcreteWaiter()
teacher = ConcreteTeacher()

builder.build_construction()
waiter.serve_the_table()
teacher.check_hometask()
