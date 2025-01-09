import math

def compute_fmod(x, y):
    if y == 0:
        return "Division by zero is not allowed"
    return math.fmod(x, y)
