from sympy.parsing.latex import parse_latex


def calculateFunction(func):
    #expr = parse_latex("\\frac{1}{\sqrt{x}}")
    expr = parse_latex(func)
    print(expr.evalf())
