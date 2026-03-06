def solution(routes):
    routes.sort(key=lambda x: x[1])
    camera_pos = routes[0][1]
    cnt = 1

    for start, end in routes[1:]:
        if start > camera_pos:
            camera_pos = end
            cnt += 1
    
    return cnt