import math

class QuadraticEquation:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def roots(self):
        discriminant = (self.b ** 2) - (4 * self.a * self.c)
        try:
            root1 = (-self.b + math.sqrt(discriminant)) / (2 * self.a)
            root2 = (-self.b - math.sqrt(discriminant)) / (2 * self.a)
            return root1, root2
        except ValueError:
            return "Non-real roots not supported yet"
        
    def y_intercept(self):
        return self.c
    
    def solve_for(self, x):
        y = self.a * x ** 2 + self.b * x + self.c
        return y

    def standard_to_vertex(self):
        h = -self.b / (2 * self.a)
        k = (4 * self.a * self.c - self.b ** 2) / (4 * self.a)
        vertex_form = f"y = {self.a}(x - {h})^2 + {k}"
        vertex = (h, k)
        opens = "up" if self.a > 0 else "down"
        return {
            "vertex_form": vertex_form,
            "vertex": vertex,
            "opens": opens
        }
