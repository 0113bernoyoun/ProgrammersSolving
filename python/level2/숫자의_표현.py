def solution(n):
    answer = 1

    for i in range(1, int(n / 2) + 1):
        sum = 0
        for j in range(i, int(n / 2) + 2):
            sum += j

            if n == sum:
                answer += 1
                break
            elif sum > n:
                break

    return answer


'''
1. 자기 자신은 무조건 가능하므로 1부터 시작
2. 절반 이상을 넘어가면 무조건 안되므로 범위를 절반으로 지정
3. 만약에 더한 값이 해당 값을 초과하는 경우도 아니므로 예외처리
'''