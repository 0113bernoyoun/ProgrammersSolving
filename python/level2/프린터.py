from collections import deque


def solution(priorities, location):
    answer = 0
    index_list = deque([i for i in range(len(priorities))])

    max_priority = max(priorities)

    while True:
        idx = index_list.popleft()
        if priorities[idx] < max_priority:
            index_list.append(idx)
        else:
            answer += 1
            priorities[idx] = 0
            max_priority = max(priorities)

            if idx == location:
                return answer




'''
deque를 순회하며 우선순위가 가장 높으면(가장 값이 크면) 출력하면서 answer에 하나를 더하고 아니면 맨 뒤로 돌려보낸다.
이 로직은 모든 출력을 할때 까지(모두 비워낼때까지) 반복한다.
만약에 이번에 출력한(pop)된 곳이 내가 원하는 위치(location)이면 그때 answer를 return 한다.
popleft()를 사용하기 위해 deque를 사용한다.
'''