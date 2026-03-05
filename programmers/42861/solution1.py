from collections import defaultdict
import heapq

def init_graph(costs):
    graph = defaultdict(list)
    
    for v1, v2, cost in costs:
        graph[v1].append((v2, cost))
        graph[v2].append((v1, cost))
    
    return graph

def solution(n, costs):
    graph = init_graph(costs)
    visited = [False] * n

    graph_weights = []
    pq = [(0, 0)]

    while pq:
        weight, vertex = heapq.heappop(pq)

        if visited[vertex]:
            continue

        visited[vertex] = True
        graph_weights.append(weight)

        for v, cost in graph[vertex]:
            heapq.heappush(pq, (cost, v))
            
    return sum(graph_weights)