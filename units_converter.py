import math


def degrees_to_rad(degree):
    rad = degree/180*math.pi
    print(f'{degree} degrees is {rad} radians.')
    return rad


d = int(input('This is a degree-radian converter. Enter degrees: '))
degrees_to_rad(d)
