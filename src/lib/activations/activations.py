import math

def relu(x):
    if isinstance(x, (int, float)):
        return max(0, x)
    if isinstance(x, list):
        return [relu(i) for i in x]

def sigmoid(x):
    if isinstance(x, (int, float)):
        return 1 / (1 + math.exp(-x))
    if isinstance(x, list):
        return [sigmoid(i) for i in x]
