def solution(A, B):
    answer = 0

    A.sort()
    B.sort(reverse=True)

    for i in range(0, len(A)):
        answer += A[i] * B[i]

    return answer


'''
가장 최소를 만들기 위해서는 가장 작은 값와 가장 큰 값을 곱하는 것이 이상적이다.
모든 리스트를 정렬하자. 단 하나의 리스트는 역순으로 정렬한다. 추후 곱셈을 편하게 하기 위해서다.
'''