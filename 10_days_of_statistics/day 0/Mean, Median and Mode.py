# -*- coding: utf-8 -*-

from scipy import stats
import numpy as np

n = int(input())
x = list(map(int, input().split()))

print(np.mean(x))
print(np.median(x))
print(int(stats.mode(x)[0]))
