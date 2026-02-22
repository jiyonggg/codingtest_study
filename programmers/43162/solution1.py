from collections import defaultdict, deque

def initialize_graph(n, computers, graph):
    for i in range(n):
        for j in range(n):
            if i != j and computers[i][j]:
                graph[i].append(j)

def solution(n, computers):
    answer = 0
    
    graph = defaultdict(list)
    initialize_graph(n, computers, graph)

    unvisited = set(range(n))
    visited = set()
    queue = deque()

    while unvisited:
        queue.append(unvisited.pop())
        
        while queue:
            vertex = queue.popleft()
            visited.add(vertex)

            if vertex in graph:
                for vertice in graph[vertex]:
                    if vertice not in visited:
                        queue.append(vertice)
        
        unvisited -= visited
        answer += 1

    return answer