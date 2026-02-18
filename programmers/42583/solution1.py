from collections import deque

def can_offboard(t, bridge):
    return bridge and (t >= bridge[0][1])

def can_onboard(bridge_weight, bridge_current_weight, truck_weight, bridge_length, bridge):
    return (bridge_weight >= (bridge_current_weight + truck_weight)) and (bridge_length > len(bridge))

def calc_truck_arrival_time(bridge_length, onboard_time):
    return onboard_time + bridge_length

def solution(bridge_length, weight, truck_weights):
    weight_queue = deque(truck_weights)
    bridge = deque()
    bridge_current_weight = 0
    t = 1

    while weight_queue:
        # 도착한 트럭 제거
        if can_offboard(t, bridge):
            end_truck = bridge.popleft()
            bridge_current_weight -= end_truck[0]

        # 올라갈 수 있는가?
        if can_onboard(weight, bridge_current_weight, weight_queue[0], bridge_length, bridge):
            truck_weight = weight_queue.popleft()
            bridge_current_weight += truck_weight
            bridge.append((truck_weight, calc_truck_arrival_time(t, bridge_length)))
            t += 1
        else:
            t = bridge[0][1]
    
    return bridge.pop()[1]