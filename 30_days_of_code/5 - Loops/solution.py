# -*- coding: utf-8 -*-
#!/bin/python3

import sys

n = int(input().strip())
x = list(range(1,11))

for i in range(10):
    x[i] = x[i] * n
    print(n, "x",i+1, "=",x[i])


