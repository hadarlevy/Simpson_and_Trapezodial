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

def Simpson(f, n, a, b):
    if n % 2 != 0:
        return 0, False
    h = (b - a) / n
    print("Error evaluation En = ", round(SimpsonError(func(), b, a, h), 6))
    integral = f(a) + f(b)
    for i in range(n):
        k = a + i * h
        if i % 2 == 0:
            integral += 2 * f(k)
        else:
            integral += 4 * f(k)
    integral *= (h/3)
    return integral, True



def SimpsonError(func,b,a,h):
    xsi = 1
    print("ƒ(x): ", func)
    f2 = sp.diff(func, x, 4)
    print("ƒ⁴: ", f2)
    diff_4 = lambdify(x, f2)
    print("ƒ⁴(", xsi, ") =", diff_4(xsi))

    return ((h**4) / 180)*(b-a)*diff_4(xsi)


def MainFunction():

    n = 4
    print("Division into sections n =", n)
    print("Numerical Integration of definite integral in range [0,𝛑] ∫= SIN(X)")
    choice = int(input(
        "Which method do you want? \n\t1.The Trapezoidal method \n\t2.Simpson’s method\n"))
    if choice == 1:
        print("I = ", round(Trapezoidal(f, n, 0, math.pi, True), 6))
    elif choice == 2:
        res = Simpson(f, n, 0, math.pi)
        if res[1]:
            print("I = ", round(res[0], 6))
        else:
            print("n must be even !")

    else:
        print("Invalid input")


MainFunction()




# See PyCharm help at https://www.jetbrains.com/help/pycharm/
