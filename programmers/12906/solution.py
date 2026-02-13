def solution(arr):
    answer = []
    
    for elem in arr:
        if (len(answer) == 0) or (elem != answer[-1]):
            answer.append(elem)

    return answer