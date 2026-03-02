from collections import defaultdict

# 잡기술: 원소 1개짜리 리스트 result를 만들어서 최솟값 갱신하기
def dfs(curr, prev, graph, n, result):
    sub_size = 1
    
    for v in graph[curr]:
        if v != prev:
            child_size = dfs(v, curr, graph, n, result)
        
            diff = abs(n - 2 * child_size)

            if diff < result[0]:
                result[0] = diff
            
            sub_size += child_size
    
    return sub_size

def solution(n, wires):
    graph = defaultdict(list)

    for v1, v2 in wires:
        graph[v1].append(v2)
        graph[v2].append(v1)
    
    result = [n]

    dfs(1, -1, graph, n, result)
    
    return result[0]