from collections import defaultdict, deque

def init_graph(wires):
    graph = defaultdict(set)

    for v1, v2 in wires:
        graph[v1].add(v2)
        graph[v2].add(v1)
    
    return graph

def count_towers(start, graph, initial_visited):
    visited = initial_visited.copy()

    queue = deque([start])
    cnt = 0

    while queue:
        v = queue.popleft()
        cnt += 1

        for tower in graph[v]:
            if tower not in visited:
                queue.append(tower)
                visited.add(tower)
    
    return cnt

def solution(n, wires):
    answer = float("inf")
    graph = init_graph(wires)

    for v1, v2 in wires:
        initial_visited = set()
        initial_visited.add(v1)
        initial_visited.add(v2)

        diff = abs(count_towers(v1, graph, initial_visited) - count_towers(v2, graph, initial_visited))
        answer = min(answer, diff)
        
    return answer