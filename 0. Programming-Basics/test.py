def sum(a, b):
    return a + b

def product(a, b):
    return a * b

def divid(a, b):
    return a / b

def sub(a, b):
    return a - b

x = int(input("Enter x: "))
y = int(input("Enter y: "))

add = sum(x, y)
mul = product(x, y)
div = divid(x, y)
s = sub(x, y)

print(add)
print(mul)
print(div)
print(s)

