# accessing module from sub-package

from packages.basic import operations
from packages.advanced import power

print("Addition:", operations.add(10, 5))
print("Subtraction:", operations.subtract(10, 5))

print("Square:", power.square(4))
print("Cube:", power.cube(3))
