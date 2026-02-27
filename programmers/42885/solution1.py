from collections import deque

def solution(people, limit):
    people = deque(sorted(people, reverse=True))

    cnt = 0

    while len(people) > 1:
        if people[0] + people[-1] <= limit:
            people.pop()
        
        people.popleft()
        cnt += 1

    return cnt + len(people)