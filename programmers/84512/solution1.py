def dfs(word, target, curr_length, curr_order):
    curr_order[0] += 1

    if word == target:
        return curr_order

    if curr_length == 5:
        return
    
    for char in "AEIOU":
        result = dfs(word+char, target, curr_length+1, curr_order)

        if result:
            return result

def solution(word):
    return dfs("", word, 0, [0])[0] - 1