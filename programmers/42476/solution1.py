from functools import cmp_to_key

def comparator(x, y):
    if str(x) + str(y) > str(y) + str(x):
        return 1
    elif str(x) + str(y) == str(y) + str(x):
        return 0
    else:
        return -1

def solution(numbers):
    # 0만 있는 경우에 대한 예외 처리
    if set(numbers) == {0}:
        return "0"
    
    numbers.sort(key=cmp_to_key(comparator), reverse=True)
    
    return "".join(map(str, numbers))