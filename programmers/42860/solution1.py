def solution(name):
    updowns = 0
    leftrights = len(name)-1
    
    for idx, char in enumerate(name):
        updowns += min(ord(char)-ord('A'), ord('Z')-ord(char)+1)

        next_non_a_index = idx + 1
        
        while next_non_a_index < len(name) and name[next_non_a_index] == 'A':
            next_non_a_index += 1
        
        leftrights = min(leftrights, idx*2+len(name)-next_non_a_index, (len(name)-next_non_a_index)*2-1+idx+1)

    return updowns + leftrights