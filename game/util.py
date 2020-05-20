import math


def clamp(my_value, min_value, max_value):
    return max(min(my_value, max_value), min_value)