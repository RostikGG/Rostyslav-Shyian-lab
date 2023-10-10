def apply(func, x, y):
    return func(x, y)

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

result1 = apply(add, 5, 3)  # Передача функції 'add' як аргументу
result2 = apply(subtract, 7, 2)  # Передача функції 'subtract' як аргументу
