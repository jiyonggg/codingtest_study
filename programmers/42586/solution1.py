def day_develop(progresses, speeds):
    for i in range(len(progresses)):
        progresses[i] += speeds[i]

def can_deploy(progresses):
    return bool(progresses) and progresses[0] >= 100

def solution(progresses, speeds):
    answer = []

    while progresses:
        day_develop(progresses, speeds)
        task_cnt = 0
        
        while can_deploy(progresses):
            progresses.pop(0)
            speeds.pop(0)
            
            task_cnt += 1
        
        if task_cnt:
            answer.append(task_cnt)
    
    return answer