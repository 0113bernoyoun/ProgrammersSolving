from itertools import combinations


def solution(nums):
    answer = 0

    permut = list(combinations(nums, 3))

    for i in permut:
        s = sum(i)
        is_decimal = True
        for i in range(2, s - 1):
            if s % i == 0:
                is_decimal = False
                break
        if is_decimal:
            answer += 1

    return answer



'''
itertools를 잘 사용하면 풀 수 있는 문제
'''