def stage_1(id):  # all string convert to lower case
    converted_id = id.lower()
    while True:
        if converted_id.find(" ") == -1:
            break

        converted_id = converted_id.replace(" ", "")

    converted_id = id.lower()
    print("stage1 :[", converted_id, "]")
    return converted_id


def stage_2(id):  # delete all character except lowercase, number, -, _, .
    converted_id = ""
    for character in id:
        if character.islower() or character.isdigit() or character == "-" or character == "_" or character == ".":
            converted_id = converted_id + character
    print("stage2 :[", converted_id, "]")
    return converted_id


def stage_3(id):  # replace .. -> .
    converted_id = id
    while True:
        converted_id = converted_id.replace("..", ".")
        if converted_id.find("..") == -1:
            break
    print("stage3 :[", converted_id, "]")
    return converted_id


def stage_4(id):  # remove first . last .
    converted_id = id

    if converted_id[0] == ".":
        converted_id = converted_id[1:]

    if len(converted_id) > 0 and converted_id[len(converted_id) - 1] == ".":
        converted_id = converted_id[:len(converted_id) - 1]

    print("stage4 :[", converted_id, "]")
    return converted_id


def stage_5(id):  # id is empty -> add a
    converted_id = id

    if len(converted_id) == 0:
        converted_id = converted_id + "a"
    print("stage5 :[", converted_id, "]")
    return converted_id


def stage_6(id):  # if id length is more than 16, remove character except 15character
    converted_id = id

    if len(converted_id) >= 16:
        converted_id = converted_id[:15]
    while True:
        if converted_id[len(converted_id) - 1] == ".":
            converted_id = converted_id[:len(converted_id) - 1]
        else:
            break

    print("stage6 :[", converted_id, "]")
    return converted_id


def stage_7(id):  # if id lengths is less than 2, add last char while id length equal 3
    converted_id = id

    if len(converted_id) <= 2:
        while len(converted_id) != 3:
            converted_id = converted_id + converted_id[len(converted_id) - 1]
    print("stage7 :[", converted_id, "]")
    return converted_id


def solution(new_id):
    answer = ''

    answer = stage_1(new_id)
    answer = stage_2(answer)
    answer = stage_3(answer)
    answer = stage_4(answer)
    answer = stage_5(answer)
    answer = stage_6(answer)
    answer = stage_7(answer)

    return answer


'''
정말 문제를 읽고 그대로만 작성해주면 되는 문제
대신 문제를 정말 꼼꼼하게 읽어야한다.
'''