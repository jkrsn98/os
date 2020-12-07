import sys
import math
from numpy import random
from heapq import *

def FCFS(arr, head):
    count = 0
    
    for i in range(len(arr)):
        cur = arr[i]
        dist = abs(cur - head)
        count = dist + count
        head = cur
        
    print('\nFCFS:\n number of movements: %s' % (count))
    
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

    for i in range(end, start - 1, -1):
        if i in requests:
            count = count + abs(pos - i)
            pos = i
            requests.remove(i)
            
    print("\nC_SCAN:\n number of movements: %s" % (count))
    
def LOOK(req, head):
    requests = req.copy()
    pos = head
    count = 0
    end = max(requests)
    start = min(requests)

    for i in range(pos, end + 1):
        if i in requests:
            count = count + abs(pos - i)
            pos = i
            requests.remove(i)

    for i in range(end, start - 1, -1):
        if i in requests:
            count = count + abs(pos - i)
            pos = i
            requests.remove(i)
            
    print("\nLOOK:\n number of movements: %s" % (count))
    
def C_LOOK(req, head):
    requests = req.copy()
    pos = head
    count = 0
    end = max(requests)
    start = min(requests)
    
    for i in range(pos, end + 1):
        if i in requests:
            count = count + abs(pos - i)
            pos = i
            requests.remove(i)
            
    count = count + abs(pos - start)
    pos = start
    
    for i in range(start, head + 1):
        if i in requests:
            count = count + abs(pos - i)
            pos = i
            requests.remove(i)

    print("\nC_LOOK:\n number of movements: %s" % (count))
    
    
arr = []

head = int(sys.argv[1])

i = 0
while i != 1000:
    r = random.randint(0, 5000)
    arr.append(r)
    i = i + 1

FCFS(arr, head)
SSTF(arr, head)
SCAN(arr, head)
C_SCAN(arr, head)
LOOK(arr, head)
C_LOOK(arr, head)