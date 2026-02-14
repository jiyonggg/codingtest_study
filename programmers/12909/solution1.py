def solution(s):
    stack = []

    for char in s:
        if not stack:
            stack.append(char)
        elif char == '(':
            stack.append(char)
        elif char == ')' and stack[-1] == '(':
            stack.pop()

    return not stack