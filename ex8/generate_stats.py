"""
In this exercise, we are going to generate data and collect statistics about it.
1. Generate 75_000 items of Product, but add ability to specify any number of items to generate. For the price use random range from 0.10 to 2.15
2. Print statistics of average price per Product. Print in a table format, for example:
+-------+--------------+
Product | AveragePrice
+-------+--------------+
Tomato  | 0.75
Potato  | 0.12
Cucumber| 1.23
Pumkin  | 2.01
Corn    | 0.16
+-------+--------------+
Try to search a package, that can make your table look great. Remember to create requirements.txt for it
4. Your code must be efficient as much as it can be, think about the RAM usage
5. Document your code with docstrings (module, classes, and functions)
"""

import random
from collections import defaultdict
from dataclasses import dataclass
from enum import IntEnum
from tabulate import tabulate

class Vegetable(IntEnum):
    """Enumeration for vegetable types."""
    Tomato = 1
    Potato = 2
    Cucumber = 3
    Pumkin = 4
    Corn = 5

@dataclass
class Product:
    """Data structure to represent a product."""
    product_id: int
    product_type: Vegetable
    product_price: float

def generate_products(num_items=75000):
    """Generate a specified number of random products."""
    products = list(Vegetable)
    for i in range(num_items):
        yield Product(
            product_id=i + 1,
            product_type=random.choice(products),
            product_price=round(random.uniform(0.10, 2.15), 2)
        )

def calculate_statistics(data):
    """Calculate the average price per product type."""
    price_summary = defaultdict(list)
    for product in data:
        price_summary[product.product_type].append(product.product_price)
    
    avg_prices = {
        product.name: round(sum(prices) / len(prices), 2)
        for product, prices in price_summary.items()
    }
    return avg_prices

def print_statistics(stats):
    """Print statistics in a formatted table."""
    table = [[product, price] for product, price in stats.items()]
    print(tabulate(table, headers=["Product", "Average Price"], tablefmt="grid"))

if __name__ == "__main__":
    data = generate_products()
    stats = calculate_statistics(data)
    print_statistics(stats)
