from itertools import cycle

def solution(answers):
    one = cycle([1, 2, 3, 4, 5])
    two = cycle([2, 1, 2, 3, 2, 4, 2, 5])
    three = cycle([3, 3, 1, 1, 2, 2, 4, 4, 5, 5])

    cnt_dict = {1: 0, 2: 0, 3: 0}

    for ans in answers:
        if next(one) == ans:
            cnt_dict[1] += 1
        
        if next(two) == ans:
            cnt_dict[2] += 1
        
        if next(three) == ans:
            cnt_dict[3] += 1
    
    answer = sorted(filter(lambda x: cnt_dict[x] == max(cnt_dict.values()), cnt_dict.keys()))
    return answer