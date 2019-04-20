from sympy.parsing.latex import parse_latex

if __name__ == '__main__':
    expr = parse_latex("\\frac{d}{dx} x^{2}")
    print(expr)
