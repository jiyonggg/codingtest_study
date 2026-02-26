from collections import deque

def solution(scoville, K):
    original = deque(sorted(scoville))
    mixed = deque()

    if original[0] >= K:
        return 0
    
    # 한 번 섞기
    mixed.append(original.popleft() + original.popleft() * 2)
    answer = 1
    
    while original and mixed:
        if mixed[0] >= K and original[0] >= K:
            return answer

        cnt = 0
        to_mix = []

        while cnt < 2:
            if not original:
                to_mix.append(mixed.popleft())
            elif not mixed:
                to_mix.append(original.popleft())
            elif original[0] <= mixed[0]:
                to_mix.append(original.popleft())
            else:
                to_mix.append(mixed.popleft())
            cnt += 1
        
        mixed.append(to_mix[0] + to_mix[1] * 2)
        answer += 1
    
    while mixed:
        if mixed[0] >= K:
            return answer
        
        if len(mixed) < 2:
            return -1
        
        mixed.append(mixed.popleft() + mixed.popleft() * 2)
        answer += 1