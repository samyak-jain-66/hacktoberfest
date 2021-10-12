class ABCFormula:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def solve(self):
        self._print_equation()
        discriminant = (self.b ** 2) - (4 * self.a * self.c)

        if discriminant > 0:
            from math import sqrt

            discriminant_root = sqrt((self.b ** 2) - (4 * self.a * self.c))
            x1 = (-self.b + discriminant_root) / (2 * self.a)
            x2 = (-self.b - discriminant_root) / (2 * self.a)
            print("x1 =", x1)
            print("x2 =", x2)

        elif discriminant == 0:
            x = -self.b / (2 * self.a)
            print("x =", x)

        else:  # discriminant < 0
            from cmath import sqrt as complex_sqrt

            discriminant_root = complex_sqrt(discriminant)
            x1 = (-self.b + discriminant_root) / (2 * self.a)
            x2 = (-self.b - discriminant_root) / (2 * self.a)
            print(f"x1 = {x1.real} + √(-1) * {x1.imag}")
            print(f"x2 = {x2.real} - √(-1) * {x2.imag}")

    def _print_equation(self):
        b_sign = "-" if self.b < 0 else "+"
        c_sign = "-" if self.c < 0 else "+"
        print(f"\n{self.a}x² {b_sign} {abs(self.b)}x {c_sign} {abs(self.c)} = 0")


ABCFormula(1, 0, -8).solve()

formula = ABCFormula(1, 2, 1)
formula.solve()

formula = ABCFormula(a=1, b=2, c=4)
formula.solve()
