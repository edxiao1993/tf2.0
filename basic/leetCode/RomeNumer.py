#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# 0<n<=3999
def rome_to_number(n):
    x = ""
    th = n // 1000
    if th > 0:
        n = n % 1000
    x = assitant(th, "th", x)
    hu = n // 100
    if hu > 0:
        n = n % 100
    x = assitant(hu, "hu", x)
    te = n // 10
    if te > 0:
        n = n % 10
    x = assitant(te, "te", x)
    x = assitant(n, "on", x)
    return x


def assitant(n, unit, x):
    if n == 0:
        return x
    one = five = ten = ""
    if unit == "th":
        for i in range(n):
            x += "M"
        return x
    if unit == "hu":
        one = "C"
        five = "D"
        ten = "M"
    elif unit == "te":
        one = "X"
        five = "L"
        ten = "C"
    elif unit == "on":
        one = "I"
        five = "V"
        ten = "X"
    return ass2(n, x, one, five, ten)


def ass2(n, x, one, five, ten):
    if n == 9:
        x += one + ten
    elif n > 5:
        x += five
        for i in range(n - 5):
            x += one
    elif n == 5:
        x += five
    elif n > 0:
        for i in range(n):
            x += one
    return x


nums = ["M", "D", "C", "L", "X", "V", "I"]
tempX = rome_to_number(3456)
print(tempX)
