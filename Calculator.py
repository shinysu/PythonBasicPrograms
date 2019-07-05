def add(x, y):
    return x + y


def subtract(x, y):
    return x - y


def multiply(x, y):
    return x * y


def divide(x, y):
    return x / y


x = 8
y = 4

print('%d + %d = %d' % (x, y, add(x, y)))
print('%d - %d = %d' % (x, y, subtract(x, y)))
print('%d * %d = %d' % (x, y, multiply(x, y)))
print('%d / %d = %d' % (x, y, divide(x, y)))