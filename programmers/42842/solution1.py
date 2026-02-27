from math import floor, sqrt

def solution(brown, yellow):
    for height in [i for i in range(1, floor(sqrt(yellow)) + 1) if not (yellow % i)]:
        width = yellow // height

        if (width + 2) * 2 + (height * 2) == brown:
            return [width+2, height+2]