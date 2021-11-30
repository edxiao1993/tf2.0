#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def number_to_rome(rome):
    n = [1000, 500, 100, 50, 10, 5, 1]
    s = 0
    i = 0
    while i < rome.__len__():
        j = get_pos(rome[i])
        x = -1
        if (i + 1) < rome.__len__():
            x = get_pos(rome[i+1])
        if x < j and x != -1:
            s = s + n[x] - n[j]
            i += 1
        else:
            s = s + n[j]
        i += 1
    return s


def get_pos(keyword):
    r = ['M', 'D', 'C', 'L', 'X', 'V', 'I']
    for i in range(r.__len__()):
        if keyword == r[i]:
            return i
    return -1


rome = "MMMCMLXXXVII"
sm = number_to_rome(rome)
print(sm)
