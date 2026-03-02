def init_uf(n):
    uf = [i for i in range(n+1)]
    rank = [0] * (n+1)

    return uf, rank

def compress_path(traversed, root, uf):
    for v in traversed:
        uf[v] = root


def find(v, uf):
    if uf[v] == v:
        return v
    
    traversed = set()
    
    while uf[v] != v:
        traversed.add(v)
        v = uf[v]
    
    compress_path(traversed, v, uf)

    return v

def union(v1, v2, uf, rank):
    v1_root = find(v1, uf)
    v2_root = find(v2, uf)

    if v1_root == v2_root:
        return
    
    if rank[v1_root] == rank[v2_root]:
        rank[v2_root] += 1
    elif rank[v1_root] < rank[v2_root]:
        v1_root, v2_root = v2_root, v1_root
    
    uf[v2_root] = v1_root

def solution(n, wires):
    answer = float("inf")

    for cut_v1, cut_v2 in wires:
        uf, rank = init_uf(n)

        for v1, v2 in wires:
            if (cut_v1, cut_v2) == (v1, v2):
                continue

            union(v1, v2, uf, rank)
        
        for i in range(1, n+1):
            find(i, uf)
        
        answer = min(answer, abs(uf.count(find(cut_v1, uf))-uf.count(find(cut_v2, uf))))
        print(answer, uf)

    return answer