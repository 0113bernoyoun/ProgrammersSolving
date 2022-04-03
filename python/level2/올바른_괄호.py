def solution(s):
    stack = []

    for i in s:

        if len(stack) == 0 and i == ')':
            return False

        if i == '(':
            stack.append(i)
        elif i == ')':
            stack.pop()

    if len(stack) != 0:
        return False

    return True


'''
괄호에 대해 언제 완벽한 괄호인지 잘 판별하면 되는 문제
'''