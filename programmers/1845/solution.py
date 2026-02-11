def solution(nums):
    pokemons = len(nums) // 2
    nums_unique = set(nums)
    return min(pokemons, len(nums_unique))