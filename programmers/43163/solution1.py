from collections import defaultdict, deque

def is_connected(a, b):
    cnt = 0

    for char_a, char_b in zip(a, b):
        if char_a != char_b:
            cnt += 1
    
    return cnt == 1

def initialize_graph(words, graph):
    for i in range(len(words)):
        for j in range(len(words)):
            if i == j:
                continue

            if is_connected(words[i], words[j]):
                graph[words[i]].append(words[j])

def solution(begin, target, words):
    if not target in words:
        return 0

    graph = defaultdict(list)
    initialize_graph(words+[begin], graph)

    queue = deque()
    visited = set()

    queue.append((0, begin))
    visited.add(begin)

    while queue:
        steps, word = queue.popleft()

        if word == target:
            return steps
        
        for next_word in graph[word]:
            if not next_word in visited:
                queue.append((steps+1, next_word))
                visited.add(next_word)

    return graph