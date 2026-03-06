def solution(N, number):
    cases = [{0}]
    
    for k in range(1, 9):
        tmp = {N*int("1"*k)}

        for j in range(1, k):
            for num1 in cases[j]:
                for num2 in cases[k-j]:
                    tmp.add(num1 + num2)
                    tmp.add(num1 - num2)
                    tmp.add(num1 * num2)
                    if num2:
                        tmp.add(num1 // num2) 
            
        if number in tmp:
            return k
        
        cases.append(tmp)

    return -1