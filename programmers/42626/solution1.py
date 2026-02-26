import heapq

def solution(scoville, K):
    answer = 0
    scoville_len = len(scoville)

    heapq.heapify(scoville)

    answer = 0

    if scoville[0] >= K:
        return answer

    while len(scoville) >= 2:
        heapq.heappush(scoville, heapq.heappop(scoville) + (heapq.heappop(scoville) * 2))
        answer += 1
        scoville_len -= 1

        if scoville[0] >= K:
            return answer

    return -1