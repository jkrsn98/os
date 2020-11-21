# Write a program the implements 3 of the following disk-scheduling algorithms:
# a. FCFS
# b. SSTF
# c. SCAN
# d. C-SCAN
# e. LOOK
# f. C-LOOK
# Your program will service a disk drive with 5,000 cylinders numbered 0-4,999.
# The program will generate a random series of 1,000 requests and service them according to three of the
# algorithms listed above. The program will be passed the initial position of the disk head as a parameter
# on the command line and report the total amount of head movement by each algorithm.

import sys
import math
from numpy import random

arr = []

head = int(sys.argv[1])

i = 0
while i != 1000:
    r = random.randint(0, 5000)
    arr.append(r)
    i = i + 1


def FCFS(arr, head):
    count = 0
    for i in range(len(arr)):
        cur = arr[i]
        dist = abs(cur - head)
        count = dist + count
        head = cur
    print('\nFCFS:\n number of movements: %s' % (count))
    
FCFS(arr, head)
