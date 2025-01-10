
"""
Poly Solver V1.01
  command line tool to perform basic operations on quadratic equations. V1.01 now uses a class to handle
  quadratic equations.

"""


import calc
import time

intro_string = """What would you like to solve?
  1. Quadratic equation
  2. Polynomial equation
  "q" - quit
selection: """
quadratic_string = """1. solve for real roots
2. find y-intercept
3. solve for value of x
4. find vertex
"b" - back
"q" - quit
selection: """


def quadratic_solver():
    print("Quadratic Solver\nInput Quadratic...")
    a = input("a: ")
    b = input("b: ")
    c = input("c: ")
    if not a or not b or not c:
        print("one or more values unfilled! try again!")
        quadratic_solver()
    try:
        a, b, c = float(a), float(b), float(c)
    except ValueError:
        print("Invalid input! Enter numbers only!")
        quadratic_solver()

    quadratic = calc.QuadraticEquation(a, b, c)
    while True:
        print(f"\nquadratic: {a}x^2 + {b}x + {c}")
        quadratic_input = input(quadratic_string)

        if quadratic_input == "1":
            print(f"roots: {quadratic.roots()}")

        elif quadratic_input == "2":
            print(f"f(0) = {quadratic.y_intercept()}")

        elif quadratic_input == "3":
            x = input("enter value of x to solve for: ")
            try:
                x = float(x)
            except ValueError:
                print("x is invalid")
                continue
            print(f"f({x}) = {quadratic.solve_for(x)}")

        elif quadratic_input == "4":
            vertex_info = quadratic.standard_to_vertex()
            print(" -Vertex form:", vertex_info["vertex_form"])
            print(" -Vertex:", vertex_info["vertex"])
            print(" -Parabola opens", vertex_info["opens"])

        elif quadratic_input == "b":
            main()
        elif quadratic_input == "q":
            print("quitting...")
            exit()
        else:
            print(f"{quadratic_input} is not a valid input! try again...")
            time.sleep(1.5)
            continue
    

def main():
    intro_input = input(intro_string)
    if intro_input == "1":
        quadratic_solver()
    elif intro_input == "2":
        # polynomial_solver()
        print("Currently Unsupported!")
        main()
    elif intro_input == "q":
        print("quitting...")
        exit()
    else:
        print(f"{intro_input} is not a valid input! try again!")
        main()


if __name__ == "__main__":
    main()


