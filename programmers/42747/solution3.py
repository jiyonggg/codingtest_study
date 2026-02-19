import bisect

def solution(citations):
    citations.sort()

    for i in range(max(citations), -1, -1):
        tmp = bisect.bisect_left(citations, i)

        if i <= len(citations) - tmp:
            return i