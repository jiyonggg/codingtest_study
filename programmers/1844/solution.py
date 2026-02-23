from collections import deque

def is_valid_position(x, y, n, m):
    return (0 <= x < n) and (0 <= y < m)

moves = [(0, 1), (1, 0), (-1, 0), (0, -1)]

def solution(maps):
    n, m = len(maps[0]), len(maps)
    goal_x, goal_y = n-1, m-1
    
    visited = set()
    queue = deque()

    # 할당할 때 3개 한 번에 flat하게 할당하기 위해 * 사용
    queue.append((1, *(0, 0)))
    visited.add((0, 0))

    while queue:
        steps, x, y = queue.popleft()

        if (x, y) == (goal_x, goal_y):
            return steps
        
        for add_x, add_y in moves:
            next_x, next_y = x+add_x, y+add_y
            if is_valid_position(next_x, next_y, n, m) and maps[next_y][next_x] and not (next_x, next_y) in visited:
                queue.append((steps+1, next_x, next_y))
                visited.add((next_x, next_y))
    
    return -1