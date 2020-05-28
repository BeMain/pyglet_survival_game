import math


def clamp(my_value, min_value, max_value):
    return max(min(my_value, max_value), min_value)

def distancesq(a, b):
    return (a[0]-b[0])**2 + (a[1]-b[1])**2