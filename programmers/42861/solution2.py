def union(v1, v2, uf, ranks):
    v1_root = find(v1, uf)
    v2_root = find(v2, uf)

    if v1_root == v2_root:
        return False
    
    if ranks[v1_root] < ranks[v2_root]:
        v1_root, v2_root = v2_root, v1_root
    elif ranks[v1_root] == ranks[v2_root]:
        ranks[v1_root] += 1
    
    uf[v2_root] = v1_root

    return True

def compress_path(root, uf, visited):
    for v in visited:
        uf[v] = root

def find(v, uf):
    visited = []

    while uf[v] != v:
        visited.append(v)
        v = uf[v]
    
    compress_path(v, uf, visited)

    return v

def solution(n, costs):
    uf = [i for i in range(n)]
    ranks = [0] * n
    weights = []

    costs.sort(key=lambda x: x[2])

    for v1, v2, cost in costs:
        if union(v1, v2, uf, ranks):
            weights.append(cost)
    
    return sum(weights)