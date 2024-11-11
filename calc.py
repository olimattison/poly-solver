import math

# quadratic equation functions:

def roots(a, b, c):
    discriminant = (b**2) - (4*a*c)
    try:
        root1 = (-b + math.sqrt(discriminant)) / 2*a
        root2 = (-b - math.sqrt(discriminant)) / 2*a
        print(f"root1: {root1} \nroot2: {root2}")
    except ValueError:
        print("Non real roots not supported yet")


def y_int(c):
    print(f"y-intercept = {c}")


def solve_for(a, b, c, x):
    print(f"solving for x = {x}")
    leading_term = x**2 * a
    middle_term = b * x
    y = leading_term + middle_term + c
    print(f"f({x}) = {y}")


def standard_to_vertex(a,b,c):
    h = -b / (2 * a)
    k = (4 * a * c - b**2) / (4 * a)
    sign_h = '+' if h < 0 else '-'
    sign_k = '+' if k >= 0 else '-'
    if a > 0:
        opens = "up"
    else:
        opens = "down"
    print(f"vertex form: y = {a}(x {sign_h} {abs(h)})^2 {sign_k} {abs(k)}")
    print(f"vertex = ({h}, {k})")
    print(f"parabola opens {opens}")

