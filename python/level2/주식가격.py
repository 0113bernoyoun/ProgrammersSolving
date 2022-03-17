def solution(prices):
    answer = [0] * len(prices)

    for i in range(len(prices)-1):
        for j in range(i, len(prices)-1):
            if prices[i] > prices[j]:
                break
            else:
                answer[i] +=1
    return answer



'''
주식이 오른건 의미없다. 그때는 break로 나오자.
만약에 주식이 떨어졌다면 해당 index의 값을 1씩 올려주면된다.
'''