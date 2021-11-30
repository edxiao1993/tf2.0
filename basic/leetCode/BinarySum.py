#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def add_binary(a, b):
    al = a.__len__() - 1
    bl = b.__len__() - 1
    most = last = 0
    if a < b:
        most = b.__len__()
        last = a.__len__()
    else:
        last = b.__len__()
        most = a.__len__()
    x = 0
    pos = last
    result = ""
    while al > 0 or bl > 0:
        s = int(a[al]) + int(b[bl]) + x
        if s >= 2:
            x = 1
            s -= 2
            result += str(s)
        else:
            x = 0
            result += str(s)
        pos -= 1
        al -= 1
        bl -= 1
    print(result)
    i = most - last
    if al < bl:
        t = list(b[:i])
        t.reverse()
        result += "".join(t)
        print(t)
    else:
        t = list(a[:i])
        t.reverse()
        result += "".join(t)
        print(t)
    print(result)


astr = "11001101"
bstr =    "10001"
add_binary(astr, bstr)
