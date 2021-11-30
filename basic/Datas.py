#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import random as rd

arrs = []
for i in range(23):
    arrs.append(rd.randint(0, 100))

for i in range(arrs.__len__()):
    for j in range(arrs.__len__() - 1):
        if arrs[j] > arrs[j+1]:
            temp = arrs[j]
            arrs[j] = arrs[j+1]
            arrs[j+1] = temp

for i in range(arrs.__len__()):
    print(str(arrs[i]))
