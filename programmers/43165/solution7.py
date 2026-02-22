def solution(numbers, target):
    memo = [[0 for _ in range((100*len(numbers))+1)] for _ in range(len(numbers))]

    memo[0][numbers[0]] = 1
    memo[0][numbers[0]*-1] = 1

    for i in range(1, len(numbers)):
        for j in range((50*len(numbers))*-1, (50*len(numbers))+1):
            memo[i][j+numbers[i]] += memo[i-1][j]
            memo[i][j-numbers[i]] += memo[i-1][j]
    
    return memo[len(numbers)-1][target]