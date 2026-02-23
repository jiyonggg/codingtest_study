from collections import deque

def get_visitable_words(current, words):
    for word in words:
        if word != current:
            cnt = 0

            for char_c, char_w in zip(current, word):
                if char_c != char_w:
                    cnt += 1
            
            if cnt == 1:
                yield word

def solution(begin, target, words):
    if not target in words:
        return 0
    
    queue = deque([begin])
    min_dist = {begin: 0}

    while queue:
        word = queue.popleft()

        if word == target:
            return min_dist[word]
        
        for visitible_word in get_visitable_words(word, words):
            if not visitible_word in min_dist:
                queue.append(visitible_word)
                min_dist[visitible_word] = min_dist[word] + 1

    return 0