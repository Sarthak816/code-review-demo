def add(a, b):
    result = a + b
    return result

def divide(a, b):
    return a / b  # Bug: No zero division check!

def calculate_average(numbers):
    total = 0
    for num in numbers:
        total = total + num
    return total / len(numbers)  # Bug: No empty list check!

# Bad naming convention
def func1(x):
    if x > 10:
        return True
    else:
        return False

# Memory inefficient
def get_large_list():
    big_list = []
    for i in range(1000000):
        big_list.append(i)
    return big_list

