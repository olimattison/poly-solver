
"""
Poly Solver V1.00
  command line tool to perform basic operations on quadratic equations. Currently supports finding real-roots,
  y-intercepts, verticies, and solving for x-values. New functions and support for higher degree polynomials
  coming soon!
"""


import calc

intro_string = """What would you like to solve?
  1. Quadratic equation
  2. Polynomial equation
  "q" - quit
selection: """
polynomial_string = """
  1. You're Cooked :(
  "b" - back
selection: """
quadratic_string = """1. solve for real roots
2. find y-intercept
3. solve for value of x
4. find vertex
"b" - back
"q" - quit
selection: """


# NOT WORKING
def polynomial_solver():
    print("Polynomail Solver\nInput Polynomial...")
    polynomial_input = input(polynomial_string)
    if polynomial_input == "1":
        pass
    elif polynomial_input == "b":
        main()
    elif polynomial_input == "q":
        print("quitting...")
        exit()
    else:
        print(f"{polynomial_input} is not a valid input! try again!")
        polynomial_solver()


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

    # quadratic solver loop
    while True:
        print(f"\nquadratic: {a}x^2 + {b}x + {c}")
        quadratic_input = input(quadratic_string)
        if quadratic_input == "1":
            calc.roots(a, b, c)
        elif quadratic_input == "2":
            calc.y_int(c)
        elif quadratic_input == "3":
            x = input("enter value of x to solve for: ")
            try:
                x = float(x)
            except ValueError:
                print("x is invalid")
                continue
            calc.solve_for(a, b, c, x)
        elif quadratic_input == "4":
            calc.standard_to_vertex(a, b, c)
        elif quadratic_input == "b":
            main()
        elif quadratic_input == "q":
            print("quitting...")
            exit()
        else:
            print(f"{quadratic_input} is not a valid input! try again!")
            quadratic_solver()


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


