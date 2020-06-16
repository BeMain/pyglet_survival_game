import math


class Vector(object):
    def __init__(self, x, y, *args, **kwargs):
        super(Vector, self).__init__(*args, **kwargs)
        
        self.x = x
        self.y = y
    
    @classmethod
    def ZERO(cls):
        return cls(0.0, 0.0)
    
    def normalize(self):
        v = math.atan2(self.y, self.x)
        self.x = math.cos(v)
        self.y = math.sin(v)


def clamp(my_value, min_value, max_value):
    return max(min(my_value, max_value), min_value)

def distancesq(vector1, vector2):
    return (vector1.x-vector2.x)**2 + (vector1.y-vector2.y)**2

def angle_between(vector1, vector2):
    x = vector1.x - vector2.x
    y = vector1.y - vector2.y
    return -math.degrees(math.atan2(y, x))
