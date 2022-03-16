
# original code : https://lagooni.tistory.com/m/entry/Python-프로그래머스-가장-큰-수-정렬
def solution(numbers):
    t_numbers = list(map(str, numbers))
    t_numbers.sort(key=lambda x: x * 3, reverse=True)
    answer = ''.join(t_numbers)
    return str(int(answer))




'''
1. list(map(str, numbers)) : numbers를 모두 문자열로 캐스팅하여 리스트에 집어넣는다.
2. 문자열로 변환한 뒤 정렬을 하는 이유는 int형으로 정렬하는 경우 9 보다 30이 큰데 문자열로 정렬하면 9가 더 우선순위가 높다.
3. 정렬을 할때 key값에 대해 3번 곱하여 비교 대상으로 한다.(문자열의 경우 3번 곱하면 해당 문자열을 3번 반복한다). 그 이유는 34, 30, 3의 경우 더 정확하게 정렬하기 위해서다.
문자열의 정렬은 각 맨 앞 글자부터 확인하게 된다.
4. 이렇게 나온 값을 합하여 return한다

'''