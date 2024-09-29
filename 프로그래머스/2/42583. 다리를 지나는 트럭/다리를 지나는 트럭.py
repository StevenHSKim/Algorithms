from collections import deque

def solution(bridge_length, weight, truck_weights):

    bridge = deque([0] * bridge_length)
    trucks = deque(truck_weights)
    
    time = 0
    current_weight = 0

    while trucks or current_weight > 0:
        time += 1
        
        # 다리의 앞부분에서 트럭이 나가면 그 무게를 빼줌
        exited_truck = bridge.popleft()
        current_weight -= exited_truck

        # 대기 트럭이 있을 때, 다리의 현재 무게가 감당 가능한 경우에 트럭을 올림
        if trucks:
            if current_weight + trucks[0] <= weight:
                # 트럭을 다리 위에 올림
                new_truck = trucks.popleft()
                bridge.append(new_truck)
                current_weight += new_truck
            else:
                # 다리가 무게를 초과하면 빈 공간을 추가 (트럭이 못 올라감)
                bridge.append(0)
    
    return time
