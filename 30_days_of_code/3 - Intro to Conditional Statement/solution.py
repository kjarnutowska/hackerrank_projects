# -*- coding: utf-8 -*-

#!/bin/python3

import sys


N = int(input().strip())

if N % 2 == 1:
    print("Weird")
else:
    if N <= 20 and N >= 6:
        print("Weird")
    else:
        print("Not Weird")

