from collections import deque
from sys import stdin

input = stdin.readline

n, l = map(int, input().split())
a = list(map(int, input().split()))

d = [0] * n

monotonic_indices = deque()

for idx, num in enumerate(a):
    if monotonic_indices:
        if monotonic_indices[0] < max(0, idx-l+1):
            monotonic_indices.popleft()
        
        while monotonic_indices and (a[monotonic_indices[-1]] > num):
            monotonic_indices.pop()

    monotonic_indices.append(idx)
    d[idx] = a[monotonic_indices[0]]

print(' '.join(map(str, d)))