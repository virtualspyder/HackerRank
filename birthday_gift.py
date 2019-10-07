
#
# n = int(input())
# s = sum(int(input()) for _ in range(n))
#
# print('%.1f' % (s / 2))


import math
import os
import random
import re
import sys


def birthday_gift(ar):
    count = 0
    big = max(ar)
    for i in range(len(ar)):
        if(ar[i] == big):
            count += 1
    return count


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    ar_count = int(input())
    ar = list(map(int, input().rstrip().split()))
    result - birthdy_gift(ar)
    fptr.write(str(result) + '\n')
    fptr.close()
