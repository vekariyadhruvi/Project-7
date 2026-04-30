import math

# Trigonometry
def trigonometry(angle):
    return {
        "sin": round(math.sin(angle), 2),
        "cos": round(math.cos(angle), 2),
        "tan": round(math.tan(angle), 2)
    }

# Factorials
def factorial(n):
    return math.factorial(n)

# Logarithms
def logarithm(num):
    return math.log10(num)

# Compound Interest
def compound_interest(p, r, t):
    amount=p*((1+r/100)**t)
    return round(amount, 2)

# Area of Circle
def area_circle(r):
    return round(math.pi*r*r, 2)

# Area of Rectangle
def area_rectangle(l, b):
    return l*b