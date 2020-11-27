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
from heapq import *

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

def SSTF(req, head):
    requests = req.copy()
    count = 0
    pos = head
    numRequests = len(requests)
    heap = []

    while len(requests) > 0:
        for r in requests:
            heappush(heap, (abs(pos - r), r))
            x = heappop(heap)[1]
            count = count + abs(pos - x)
            pos = x
            requests.remove(x)
            heap = []
    print("\nSSTF:\n number of movements: %s" % (count))


SSTF(arr, head)

def SCAN(req, head):
    requests = req.copy()
    count = 0
    pos = head
    end = 4999
    start = 0
    for i in range(pos, end + 1):
        if i in requests:
            count + abs(pos - i)
            pos = i
            requests.remove(i)
    count = count + abs(pos - end)
    pos = end
    for i in range(end, start - 1, -1):
        if i in requests:
            count += abs(pos - i)
            pos = i
    print("\nSCAN:\n number of movements: %s" % (count))


SCAN(arr, head)

def C_SCAN(req, head):
    requests = list(req)
    pos = head
    count = 0
    end = max(requests)
    start = min(requests)
    for i in range(pos, end + 1):
        if i in requests:
            count = count + abs(pos - i)
            pos = i
            requests.remove(i)

    #seek back to start
    for i in range(end, start - 1, -1):
        if i in requests:
            count = count + abs(pos - i)
            pos = i
            requests.remove(i)
    print("\nC_SCAN:\n number of movements: %s" % (count))


C_SCAN(arr, head)