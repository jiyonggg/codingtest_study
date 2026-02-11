def solution(participant, completion):
    counter = dict()
    
    for p in participant:
        if p not in counter:
            counter[p] = 0
        counter[p] += 1
    
    for c in completion:
        counter[c] -= 1
        if not counter[c]:
            del counter[c]

    not_completion = list(counter.keys())[0]
    return not_completion