def solution(progresses, speeds):
    # q에 담기는 것: (경과 일수, 배포 기능 개수)
    q = []
    
    for progress, speed in zip(progresses, speeds):
        if not q or q[-1][0] < -((progress - 100) // speed):
            q.append([-((progress - 100) // speed), 1])
        else:
            q[-1][1] += 1
    
    return [elem[1] for elem in q]