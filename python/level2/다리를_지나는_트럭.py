from collections import deque


def solution(bridge_length, weight, truck_weights):
    truck_weights = deque(truck_weights)
    bridge = deque([0 for _ in range(bridge_length)])
    time = 0
    bridge_weight = 0

    while len(bridge) != 0:
        passed_truck = bridge.popleft()  # bridge에서 truck 나감
        bridge_weight -= passed_truck
        time += 1

        if truck_weights:  # 아직 못 통과한 truck이 있다면
            if bridge_weight + truck_weights[0] <= weight:
                in_truck = truck_weights.popleft()
                bridge_weight += in_truck
                bridge.append(in_truck)  # bridge에 truck 올림
            else:
                bridge.append(0)

    return time


'''
내가 잘못생각한 점
- 리스트에서 시간이 지나갈때 한번에 한 idx씩 지나가는걸로 착각함
'''