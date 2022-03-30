def solution(price, money, count):

    return sum([price * i for i in range(1, count + 1)]) - money if  sum([price * i for i in range(1, count + 1)]) - money > 0 else money - sum([price * i for i in range(1, count + 1)])


'''
문제 자체는 쉬우므로 어떻게 하면 한줄로 끝낼 수 있을까 고민하다가... 삼항연산자랑 sum함수의 합작
'''