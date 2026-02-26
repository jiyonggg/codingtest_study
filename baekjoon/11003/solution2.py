import heapq
from sys import stdin

input = stdin.readline

n, l = map(int, input().split())
a = list(map(int, input().split()))
d = []

priority_queue = []


for idx, num in enumerate(a):
    while priority_queue and priority_queue[0][1] < max(0, idx-l+1):
        heapq.heappop(priority_queue)
    
    heapq.heappush(priority_queue, (num, idx))
    d.append(priority_queue[0][0])

print(*d)