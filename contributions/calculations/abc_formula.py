def abc_formula(a, b, c):
    print_equation(a, b, c)
    discrimitant = (b ** 2) - (4 * a * c)
    if discrimitant > 0:
        from math import sqrt

        discriminant_root = sqrt((b ** 2) - (4 * a * c))
        x1 = (-b + discriminant_root) / (2 * a)
        x2 = (-b - discriminant_root) / (2 * a)
        print("x1 =", x1)
        print("x2 =", x2)

    elif discrimitant == 0:
        x = -b / (2 * a)
        print("x =", x)
    else:  # discriminant < 0
        from cmath import sqrt as complex_sqrt

        discriminant_root = complex_sqrt(discrimitant)
        x1 = (-b + discriminant_root) / (2 * a)
        x2 = (-b - discriminant_root) / (2 * a)
        print(f"x1 = {x1.real} + √(-1) * {x1.imag}")
        print(f"x2 = {x2.real} - √(-1) * {x2.imag}")


def print_equation(a, b, c):
    b_sign = "-" if b < 0 else "+"
    c_sign = "-" if c < 0 else "+"
    print(f"\n{a}x² {b_sign} {abs(b)}x {c_sign} {abs(c)} = 0")


abc_formula(1, 0, -8)
abc_formula(1, 2, 1)
abc_formula(a=1, b=2, c=4)
