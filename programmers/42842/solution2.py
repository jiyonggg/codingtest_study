from math import sqrt

def solution(brown, yellow):
    yellow_w = (-(4-brown) + sqrt((4-brown)**2-16*yellow)) // 4
    yellow_h = yellow // yellow_w

    return [yellow_w+2, yellow_h+2]