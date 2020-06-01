import math


def clamp(my_value, min_value, max_value):
    return max(min(my_value, max_value), min_value)

def distancesq(a, b):
    return (a[0]-b[0])**2 + (a[1]-b[1])**2

def angle_between(pos1, pos2):
    x = pos1[0] - pos2[0]
    y = pos1[1] - pos2[1]
    return -math.degrees(math.atan2(y, x))
