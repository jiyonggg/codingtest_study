def solution(numbers, target):
    answer = 0

    for i in range(2**len(numbers)):
        tmp = []

        for j in range(len(numbers)):
            if not (i & 2**j):
                tmp.append(numbers[j])
            else:
                tmp.append(numbers[j]*-1)
        
        if sum(tmp) == target:
            answer += 1
    
    return answer