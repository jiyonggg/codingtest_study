from collections import deque

def solution(bridge_length, weight, truck_weights):
    bridge = deque(0 for _ in range(bridge_length))
    truck_queue = deque(truck_weights)
    current_weights = 0
    current_trucks = 0
    time = 0

    while truck_queue:
        if (end_truck_weight := bridge.popleft()) > 0:
            current_weights -= end_truck_weight
            current_trucks -= 1

        if current_weights + truck_queue[0] <= weight and current_trucks < bridge_length:
            truck_weight = truck_queue.popleft()
            bridge.append(truck_weight)
            current_weights += truck_weight
            current_trucks += 1
        else:
            bridge.append(0)
    
        time += 1

    while bridge:
        bridge.pop()
        time += 1
    
    return time