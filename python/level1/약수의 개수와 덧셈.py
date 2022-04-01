def solution(left, right):
    answer = 0

    for number in range(left, right + 1):
        cnt = 0
        for j in range(1, number + 1):
            if number % j == 0:
                cnt += 1
        if cnt % 2 == 0:
            answer += number
        else:
            answer -= number

    return answer


'''
어설프게 머리를 굴리면 오히려 틀리는 문제
자연스럽게 1과 자기자신은 빼면 될거라고 생각했지만 오히려 그게 발목을 잡는다.
'''