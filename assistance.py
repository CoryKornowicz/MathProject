from sympy import *


def cos_taylor(x, n, previous):
    return cos.taylor_term(n, x, previous)


def sin_taylor(x, n, previous):
    return sin.taylor_term(n, x, previous)


def atan_taylor(x, n, previous):
    return atan.taylor_term(n, x, previous)


def e_taylor(x, n, previous):
    return exp(x).taylor_term(n, x, previous)


def ln_taylor(x, n , previous):
    return ln(x).taylor_term(n, x, previous)


def one_over_taylor(x, n):
    expr = (1/1-x)
    return taylor(expr, x, n)
    # return summation(x**n, (n, 0, oo))


# Taylor approximation at x0 of the function 'function'
def taylor(func, x0, n, x=sympy.Symbol('x')):
    i = 0
    p = 0
    while i <= n:
        p = p + (func.diff(x, i).subs(x, x0)) / (factorial(i)) * (x - x0) ** i
        i += 1
    return p


# def summation_taylor(f, x, a, b, n):
#     func = (f.diff(x, n).subs(x, a)) / (factorial(n)) * (x - a) ** n
#     return summation(func, (n, a, b))