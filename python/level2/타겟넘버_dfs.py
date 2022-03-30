counter = 0


def dfs(idx, sum_value, target, numbers):
    global counter

    if idx == len(numbers) and target == sum_value: # idx == len(numbers)인 이유는 처음에 0부터 시작을 했기 때문이다.
        counter += 1
        return
    if idx == len(numbers):
        return

    dfs(idx + 1, sum_value - numbers[idx], target, numbers)
    dfs(idx + 1, sum_value + numbers[idx], target, numbers)


def solution(numbers, target):
    global counter

    dfs(0, 0, target, numbers)

    return counter


'''
실은 내가 손을 못대는 부분은 dfs/bfs이다. 이론은 알겠는에 어떻게 써먹어야할지 생각이 잘 나지 않는다.
타겟넘버 문제는 주어진 값들을 더하고 빼면서 전부 계산한 결과가 특정 값과 일치하는지 확인하는 문제다.

처음에는 0으로 시작해서 실제 값이 있는 idx에 접근하는 순간 dfs를 2개로 나누어 진행한다.
다음 숫자에 대해 더하거나 빼는 선택지가 있기 때문이다.

이렇게 재귀함수를 통해 점점 값이 불어나면 중단점이 있어야 한다.
그래서 idx == len(numbers)로 체크를 한다. 보통은 idx == len(numbers) - 1 이라 하지만 우리는 처음에 0부터 시작해서
처음 숫자 부터 음수, 양수 분기를 나누어 진행한다. 그래서 idx == len(numbers)이다.
'''