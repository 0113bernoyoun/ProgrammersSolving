import math


def solution(n):
    answer = 0
    rst = [True] * (n + 1)

    for i in range(2, int(math.sqrt(n)) + 1):
        if rst[i] == True:
            j = 2
            while i * j <= n:
                rst[i * j] = False
                j += 1
    for i in range(2, n + 1):
        if rst[i]:
            answer += 1

    return answer



'''
단순히 소수를 찾는게 문제가 아닌 효율성 있게 찾는 것이 관건인 문제
에라토스테네스의 체 알고리즘을 사용했다.

에라토스테네스의 체 설명
* 2부터 소수를 구하고자 하는 모든 수를 나열한다.
* 범위 수의 제곱근까지만 구하면 된다.
* 기존 수에 2부터 하나씩 올려가며 곱한 수는 소수가 아니므로 False로 체크한다.
* 위 과정을 반복한다.
'''

#기존 작성 코드
'''
def solution(n):
    answer = 0
    
    if n == 2:
        answer = 1
    else :
        answer = 1
        for i in range(3, n + 1) :
            is_prime_num = True
            for j in range(2, i) :
                if i%j == 0 :
                    is_prime_num = False
                    break
                    
            if is_prime_num == True :
                answer = answer + 1
        
    return answer

'''