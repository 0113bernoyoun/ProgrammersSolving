from collections import deque

count = 0


def bfs(numbers, target):
    global count
    queue = deque()
    idx = 0
    sum_value = 0
    queue.append((sum_value + numbers[idx], idx))
    queue.append((sum_value - numbers[idx], idx))

    while queue:
        sum_value, idx = queue.popleft()

        idx += 1
        if idx < len(numbers):
            queue.append((sum_value - numbers[idx], idx))
            queue.append((sum_value + numbers[idx], idx))
        else:
            if sum_value == target:
                count += 1


def solution(numbers, target):
    global count
    bfs(numbers, target)

    return count


'''
dfs보다 이해가 더 어려웠다. 근데 잘 생각해보니 이해가 가더라..
그냥 당장 할 수 있는 것들을 다 queue에 넣어가면서 조건에 맞춰 결과물을 확인만 하면 되는 것이였다.
조건에 안맞으면 queue에 넣고 계속 순차적으로 수행하면 된다. 조건에 안맞을 경우 queue에서 pop만 하다 반복문이 끝난다.
'''