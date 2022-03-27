def solution(n, arr1, arr2):
    answer = []

    for i in range(0, n):
        result = ""

        or_operation_result = bin(arr1[i] | arr2[i])
        or_operation_result = or_operation_result.replace('0b', '')

        if len(or_operation_result) != n:
            while len(or_operation_result) != n:
                or_operation_result = "0" + or_operation_result

        for idx in or_operation_result:
            if idx == "1":
                result += "#"
            else:
                result += " "

        answer.append(result)

    return answer

'''
or 비트연산과 bin 함수를 알고 있다면 쉽게 풀 수 있는 문제
암호의 해독은 두 지도의 같은 행을 or연산했을 때 나오는 값이다.
각 값을 | (or 비트연산자)를 이용해 값을 구해서 bin함수를 이용해 2진수로 출력한다
나는 앞에 2진수를 나타내는 문자열 '0b'는 필요가 없으니 제거한다.
암호를 풀려면 1은 #, 0은 공백으로 바꿔줘야하는데 연산 과정에서 길이가 맞지 않을 수 있다.
길이가 n 보다 작다면 맞추기 위해 앞에 '0'을 더해준다.
'''