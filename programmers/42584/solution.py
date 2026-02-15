def can_pop(stack, price):
    return stack and (stack[-1][1] > price)

def solution(prices):
    answer = [i for i in range(len(prices)-1, -1, -1)]

    stack = []

    for idx, price in enumerate(prices):
        while can_pop(stack, price):
            past_idx, _ = stack.pop()

            answer[past_idx] = idx - past_idx
        
        stack.append((idx, price))
    
    return answer