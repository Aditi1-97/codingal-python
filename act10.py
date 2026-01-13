class ExpSolver:
    def __init__(self, a, b, c, d):
        self.a = a
        self.b = b
        self.c = c
        self.d = d

    def solve(self):
        result = (self.a + self.b) * self.c - self.d
        return result

obj = ExpSolver(5, 3, 2, 4)

print("Result of the expression is:", obj.solve())
