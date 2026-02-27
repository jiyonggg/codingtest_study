from math import floor, sqrt

def is_prime(num):
    if num < 2:
        return False
    
    return all(num % i for i in range(2, floor(sqrt(num))+1))

def use_card(current_num_str, remaining, primes):
    if current_num_str:
        current_num = int(current_num_str)
    
        if is_prime(current_num):
            primes.add(current_num)
    
    for i in range(len(remaining)):
        use_card(current_num_str+remaining[i], remaining[:i]+remaining[i+1:], primes)

def solution(numbers):
    primes = set()
    use_card("", numbers, primes)
    
    return len(primes)