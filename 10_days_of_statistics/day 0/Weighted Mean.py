# -*- coding: utf-8 -*-

N = int(input())
x = list(map(int, input().split()))
w = list(map(int, input().split()))

weighted_sum = 0
for i in range(N):
    weighted_sum = weighted_sum + x[i] * w[i]

print(round(weighted_sum / sum(w),1))