ZERO = "zero"
ONE = "one"
TWO = 'two'
THREE = 'three'
FOUR = 'four'
FIVE = 'five'
SIX = 'six'
SEVEN = 'seven'
EIGHT = 'eight'
NINE = 'nine'


def solution(s):
    s = s.replace(ZERO, "0")
    s = s.replace(ONE, "1")
    s = s.replace(TWO, "2")
    s = s.replace(THREE, "3")
    s = s.replace(FOUR, "4")
    s = s.replace(FIVE, "5")
    s = s.replace(SIX, "6")
    s = s.replace(SEVEN, "7")
    s = s.replace(EIGHT, "8")
    s = s.replace(NINE, "9")

    return int(s)



'''
이 문제를 깔끔하게 풀까 그냥 노가다로 풀까 고민했다.
어처피 저 행동만 하는거라면 복잡하게 갈 필요 없이 노가다가 더 효율적이기 때문이다.
'''