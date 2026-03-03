def solution(word):
    vowels = "AEIOU"
    answer = 0

    weights = [781, 156, 31, 6, 1]
    
    for (i, char) in enumerate(word):
        answer += vowels.index(char) * weights[i] + 1
    
    return answer