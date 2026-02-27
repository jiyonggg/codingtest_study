from itertools import permutations

def solution(numbers):
    used = []
    cnt = 0

    for i in range(1, len(numbers)+1):
        for elem in permutations(numbers, i):
            num = int(''.join(elem))
            
            if not num in used:
                used.append(num)
                if num > 1:
                    for i in range(2, num):
                        if not (num % i):
                            break
                    else:
                        cnt += 1

    return cnt