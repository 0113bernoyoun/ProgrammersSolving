def solution(absolutes, signs):
    answer = 0
    for i in range(0, len(absolutes)) :
        if signs[i] == True :
            answer = answer + absolutes[i]
        else :
            answer = answer - absolutes[i]
    return answer


'''
문제 풀다가 골때렸던 문제.
true, false가 문자열인줄 알았다가 계속 실패해서 알고보니 진짜 boolean임
'''