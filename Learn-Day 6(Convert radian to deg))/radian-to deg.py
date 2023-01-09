import math


def formula(radian):
    deg = radian * (180/math.pi)
    print(deg)


rad = float(input("Enter the radian that you waant to convert: "))
formula(rad)
