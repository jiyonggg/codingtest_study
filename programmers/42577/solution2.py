def solution(phone_book):
    exists = dict()

    for tel in phone_book:
        exists[tel] = 1

    for tel in phone_book:
        for i in range(1, len(tel)):
            if (tel[:i] in exists):
                return False
    
    return True