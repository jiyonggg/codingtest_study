def get_to_remove(number, k):
    monotonic = []
    to_remove = []
    to_remove_cnt = 0

    for idx, num in enumerate(number):
        while monotonic and number[monotonic[-1]] < num:
            prev_idx = monotonic.pop()
            to_remove.append(prev_idx)
            to_remove_cnt += 1

            if to_remove_cnt == k:
                return sorted(to_remove, reverse=True)
        
        monotonic.append(idx)
    
    return to_remove


def solution(number, k):
    answer = ""
    to_remove = get_to_remove(number, k)
    
    answer_str_len = 0
    final_str_len = len(number) - k
    
    for idx, num in enumerate(number):
        if to_remove and to_remove[-1] == idx:
            to_remove.pop()
            continue

        answer += num
        answer_str_len += 1

        if answer_str_len == final_str_len:
            break
    
    return answer