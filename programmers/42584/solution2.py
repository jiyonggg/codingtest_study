import heapq

def solution(prices):
    priority_queue = []
    answer = [i for i in range(len(prices)-1, -1, -1)]

    for idx, price in enumerate(prices):
        price = -price
        
        while priority_queue and priority_queue[0][0] < price:
            _, prev_idx = heapq.heappop(priority_queue)
            answer[prev_idx] = idx - prev_idx
        
        heapq.heappush(priority_queue, (price, idx))
    
    return answer