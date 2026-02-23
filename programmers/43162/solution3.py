def compress_path(traversed, root, uf):
    for vertex in traversed:
        uf[vertex] = root

def find_root(vertex, uf):
    traversed = set()

    while vertex != uf[vertex]:
        traversed.add(vertex)
        vertex = uf[vertex]
    
    compress_path(traversed, vertex, uf)

    return vertex

def union(x, y, uf, ranks):
    root_x = find_root(x, uf)
    root_y = find_root(y, uf)

    if root_x == root_y:
        return
    
    if ranks[root_x] == ranks[root_y]:
        if root_x > root_y:
            root_x, root_y = root_y, root_x
        ranks[root_x] += 1
    elif ranks[root_x] < ranks[root_y]:
        root_x, root_y = root_y, root_x
    
    uf[root_y] = root_x
    
def initialize_uf(n, computers, uf, ranks):
    for i in range(n):
        for j in range(n):
            if i != j and computers[i][j]:
                union(i, j, uf, ranks)

def solution(n, computers):
    uf = [i for i in range(n)]
    ranks = [0 for _ in range(n)]

    initialize_uf(n, computers, uf, ranks)

    return len(set(find_root(i, uf) for i in range(n)))