#praca domowa lab1

import math


x: int = int(input("Type x:"))
y: int = int(input("Type y:"))
z: int = int(input("Type z:"))

powX = x ** 2
powY = y ** 2
powZ = z ** 2

rad = math.sqrt(powX + powY + powZ)
widthInSphere = math.atan(y / x)
lengthInSphere = math.acos(z / rad)

print("Spherical coordinates:")
print("radius=" + str(rad))
print("width=" + str(widthInSphere))
print("length=" + str(lengthInSphere))

p = math.sqrt(powX + powY)
angle = math.atan(x / y)
z = z

print("Cylindrical coordinates:")
print("p=" + str(p))
print("angle=" + str(angle))
print("z=" + str(z))

