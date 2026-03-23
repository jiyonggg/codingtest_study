from math import trunc

def find_available_min_idx(time, jobs):
    idx = 0

    while idx < len(jobs):
        if time >= jobs[idx][1][0]:
            return idx
        
        idx += 1
    
    return -1

def solution(jobs):
    # [idx, [요청 시간, 소요 시간]]
    jobs_with_no = sorted(enumerate(jobs), key=lambda x: (x[1][1], x[1][0], x[0]))

    time = -1
    current_task = []
    total = 0

    while (jobs_with_no or current_task):
        time += 1

        if current_task and current_task[0][0] == time:
            finished_job = current_task.pop()
            total += (time - finished_job[1])

        if jobs_with_no and not current_task:
            job_idx = find_available_min_idx(time, jobs_with_no)
            
            if job_idx == -1:
                continue

            job = jobs_with_no.pop(job_idx)
            # (끝나는 시간, 요청 시간)
            current_task.append((time+job[1][1], job[1][0]))

    return trunc(total / len(jobs))