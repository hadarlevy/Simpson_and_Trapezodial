# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
# This is a sample Python script.


import sympy as sp
import math
from sympy.utilities.lambdify import lambdify
x = sp.symbols('x')



def Trapezoidal(f, n, a, b, tf):
    h = (b - a) / n
    if tf:
        print("Error evaluation En = ", round(TrapezError(func(), b, a, h), 6))
    integral = 0.5 * (f(a)*f(b))
    for i in range(n):
        integral += f(a+h*i)
    integral *= h
    return integral





def func():
    # we need to change it according to the question
    return sp.sin(x)


def f(val):
    return lambdify(x, func())(val)


def TrapezError(func, b, a, h):
    xsi = (-1)*(math.pi/2)
    print("ƒ(x): ", func)
    f2 = sp.diff(func, x, 2)
    print("ƒ'': ", f2)
    diff_2 = lambdify(x, f2)
    print("ƒ''(", xsi, ") =", diff_2(xsi))
    return h**2/12*(b-a)*diff_2(xsi)






# See PyCharm help at https://www.jetbrains.com/help/pycharm/
