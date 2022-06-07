# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
# This is a sample Python script.


import sympy as sp
import math
from sympy.utilities.lambdify import lambdify
x = sp.symbols('x')



def TrapezoidalRule(f, n, a, b, tf):
    """
    rapezoidal Rule is a rule that evaluates the area under the curves by dividing the total area
    into smaller trapezoids rather than using rectangles
    :param f: The desired integral function
    :param n: The division number
    :param a: Lower bound
    :param b: Upper bound
    :param tf: Variable to decide whether to perform Error evaluation
    :return: The result of the integral calculation
    """
    h = (b - a) / n
    if tf:
        print("Error evaluation En = ", round(TrapezError(func(), b, a, h), 6))
    integral = 0.5 * (f(a)*f(b))
    for i in range(n):
        integral += f(a+h*i)
    integral *= h
    return integral


def func():
    return sp.sin(x)


def f(val):
    return lambdify(x, func())(val)


def TrapezError(func, b, a, h):
    """
    The trapezoidal rule is a method for approximating definite integrals of functions.
    The error in approximating the integral of a twice-differentiable function by the trapezoidal rule
    is proportional to the second derivative of the function at some point in the interval.
    :param func: The desired integral function
    :param b: Upper bound
    :param a: Lower bound
    :param h: The division
    :return: The error value
    """
    xsi = (-1)*(math.pi/2)
    print("ƒ(x): ", func)
    f2 = sp.diff(func, x, 2)
    print("ƒ'': ", f2)
    diff_2 = lambdify(x, f2)
    print("ƒ''(", xsi, ") =", diff_2(xsi))
    return h**2/12*(b-a)*diff_2(xsi)







# See PyCharm help at https://www.jetbrains.com/help/pycharm/
