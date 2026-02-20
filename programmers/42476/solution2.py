def solution(numbers):
    # 0만 있는 경우에 대한 예외 처리
    if set(numbers) == {0}:
        return "0"
    
    numbers.sort(key=lambda x: str(x)*3, reverse=True)

    return "".join(map(str, numbers))