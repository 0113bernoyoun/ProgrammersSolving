def solution(s):
    answer = 0

    had_repeat_char = False
    stack = []

    for i in s:
        if stack:
            last_item = stack[len(stack) - 1]

            if last_item == i:
                stack.pop()
            else:
                stack.append(i)
        else:
            stack.append(i)

    if stack:
        return 0
    else:
        return 1


'''
stack을 사용하면 상당히 편하게 풀 수 있는 문제
'''