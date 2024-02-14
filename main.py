from multiplier.mult import mult
from adder.add import add
import logging

logging.basicConfig(level=logging.DEBUG)

num_a = int(input("Enter a number: "))
num_b = int(input("Enter another number: "))

print(f"Output: {add(num_a, mult(num_a, num_b))}")