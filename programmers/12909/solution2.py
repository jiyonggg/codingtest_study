def solution(s):
    bracket_balance = 0

    for char in s:
        if char == '(':
            bracket_balance += 1
        elif char == ')':
            bracket_balance -= 1
        
        if bracket_balance < 0:
            return False

    return not bracket_balance