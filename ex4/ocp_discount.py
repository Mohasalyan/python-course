# Open/Closed Principle (OCP)

class Discount:
    """
    Base class for discount calculation.
    """
    def __init__(self, price: float):
        self.price = price

    def give_discount(self) -> float:
        return self.price


class SilverDiscount(Discount):
    def give_discount(self) -> float:
        return self.price * 0.8  # 20% discount


class GoldDiscount(Discount):
    def give_discount(self) -> float:
        return self.price * 0.7  # 30% discount


class VIPDiscount(Discount):
    def give_discount(self) -> float:
        return self.price * 0.6  # 40% discount


# Example Usage
silver = SilverDiscount(100)
gold = GoldDiscount(100)
vip = VIPDiscount(100)

print(f"Silver Price: {silver.give_discount()}")  # 80
print(f"Gold Price: {gold.give_discount()}")  # 70
print(f"VIP Price: {vip.give_discount()}")  # 60
