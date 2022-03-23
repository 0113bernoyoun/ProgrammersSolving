ENTER_KEYWORD = "Enter"
LEAVE_KEYWORD = "Leave"
CHANGE_KEYWORD = "Change"

ENTER_MESSAGE = "님이 들어왔습니다."
LEAVE_MESSAGE = "님이 나갔습니다."


def solution(record):
    answer = []
    user_list = {} # user의 id와 이름을 관리
    command_list = [] #명령어를 user의 id와 함께 관리

    for i in record:
        data = i.split(' ')

        if data[0] == ENTER_KEYWORD:
            user_list[data[1]] = data[2]
            command_list.append([data[1], ENTER_KEYWORD])  # id, action 순
        elif data[0] == CHANGE_KEYWORD:
            user_list[data[1]] = data[2]
        elif data[0] == LEAVE_KEYWORD:
            command_list.append([data[1], LEAVE_KEYWORD])

    for i in command_list:  # id와 이름은 user_list에 매핑되어있음
        name = user_list[i[0]]
        if i[1] == ENTER_KEYWORD:
            log = name + ENTER_MESSAGE
            answer.append(log)
        elif i[1] == LEAVE_KEYWORD:
            log = name + LEAVE_MESSAGE
            answer.append(log)

    return answer