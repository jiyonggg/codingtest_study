def solution(answers):
    one = [1, 2, 3, 4, 5]
    two = [2, 1, 2, 3, 2, 4, 2, 5]
    three = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]

    cnt_dict = {1: 0, 2: 0, 3: 0}

    for idx, ans in enumerate(answers):
        if one[idx % len(one)] == ans:
            cnt_dict[1] += 1
        
        if two[idx % len(two)] == ans:
            cnt_dict[2] += 1
        
        if three[idx % len(three)] == ans:
            cnt_dict[3] += 1
    
    answer = sorted(filter(lambda x: cnt_dict[x] == max(cnt_dict.values()), cnt_dict.keys()))
    return answer