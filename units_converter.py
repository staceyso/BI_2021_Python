import math


def rad_to_degrees(rad):
    degree = rad*180/math.pi
    print(f'{rad} radians is {degree} degrees.')
    return degree


r = int(input('This is radian-degree converter. Enter the angle in radians: '))
rad_to_degrees(r)
