#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def two_sum(a, target):
    for i in range(a.__len__() - 1):
        for j in range(i, a.__len__()):
            if a[i] + a[j] == target:
                return i, j


a = [2, 7, 11, 15, 90]
target = 9
ts = two_sum(a, target)
print(ts)
