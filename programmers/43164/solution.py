from collections import defaultdict

def dfs(start, graph, path, unvisited, n):
    path.append(start)

    if len(path) == n + 1:
        return path

    for airport in sorted(graph[start]):
        if [start, airport] in unvisited:
            unvisited.remove([start, airport])

            rt = dfs(airport, graph, path, unvisited, n)
            
            if rt:
                return rt
            
            unvisited.append([start, airport])

    path.pop()

def initialize_graph(tickets, graph):
    for start, end in tickets:
        graph[start].add(end)

def solution(tickets):
    graph = defaultdict(set)
    initialize_graph(tickets, graph)

    return dfs("ICN", graph, [], tickets, len(tickets))