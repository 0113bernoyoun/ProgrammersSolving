def solution(arr):
    answer = []

    comp_number = arr[0]
    answer.append(comp_number)
    for i in range(1, len(arr)):
        if comp_number == arr[i]:
            continue
        else:
            comp_number = arr[i]
            answer.append(comp_number)

    return answer





'''
여기서 더 숏코딩이 가능할 것 같은데.. 다른 사람 코드 안보고 한번 고민해봐야겠다..
'''