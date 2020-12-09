import sys
import math
from numpy import random
from heapq import *

def FCFS(req, head):
    count = 0
    
    for i in range(len(req)):
        cur = req[i]
        dist = abs(cur - head)
        count = dist + count
        head = cur
        
    print('\nFCFS:\n number of movements: %s' % (count))
    
def SSTF(req, head):
    requests = req.copy()
    pos = head
    count = 0

    while requests:
        closest = abs(pos - requests[0])
        closestIndex = 0
        for x in range(1, len(requests)):
            if abs(pos - requests[x]) < closest:
                closest = abs(pos - requests[x])
                closestIndex = x
        count += abs(pos - requests[closestIndex])
        pos = requests[closestIndex]
        requests.remove(pos)   
    print("\nSSTF:\n number of movements: %s" % (count))
    
def SCAN(req, head):
    requests = req.copy()
    count = 0
    pos = head
    direction = 'r'
    
    while requests:
        if pos in requests:
            requests.remove(pos)

            if not requests:
                break
        if direction == 'l' and pos > 0:
            pos = pos - 1
        if direction == 'r' and pos < 4998:
            pos = pos + 1

        count = count + 1

        if pos == 0:
            direction = 'r'
        if pos == 4998:
            direction = 'l'
            
    print("\nSCAN:\n number of movements: %s" % (count))
    
def C_SCAN(req, head):
    requests = req.copy()
    pos = head
    count = 0
    while requests:
        if pos in requests:
            requests.remove(pos)
            if not requests:
                break

        count = count + 1
        pos = pos + 1
        if pos == 4998:
            pos = 0
            count = count + 4998
            
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