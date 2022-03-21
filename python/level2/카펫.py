def solution(brown, yellow):
    yellow_width = 1

    while True:
        yellow_height = 1
        while yellow_width >= yellow_height:
            if (yellow_width * 2) + (yellow_height * 2) + 4 == brown and yellow_width * yellow_height == yellow:
                return [yellow_width + 2, yellow_height + 2]
            else:
                yellow_height += 1

        yellow_width += 1



'''
이 문제는 완전탐색으로 풀어야 한다.
yellow의 가로,세로를 기준으로 완전 탐색을 진행한다.

우선 전체 brown의 개수는 노란색의 가로 * 2 + yellow * 2 + 4(꼭짓점)이다.
이후 height의 길이를 늘려가며 계속 비교를 한다.
조건으로 width >= height의 조건이 달려있다.

만약 height가 width보다 커지면 width를 1 늘려주고 다시 처음부터 비교를 시작한다. 

그리고 카펫의 가로,세로 길이는 yellow의 가로와 세로에서 2씩 더한 값이 된다.
'''