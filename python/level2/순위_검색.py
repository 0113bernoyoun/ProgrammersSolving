def solution(info, query):
    answer = []
    lang_list = ["cpp", "java", "python"]
    part = ["backend", "frontend"]
    career = ["junior", "senior"]
    soulfood = ["chicken", "pizza"]
    answer = [0] * len(query)

    for i in info:
        i_data = i.split(" ")
        i_lang = i_data[0]
        i_part = i_data[1]
        i_career = i_data[2]
        i_soulfood = i_data[3]
        i_score = i_data[4]

        for q in range(0, len(query)):
            q_data_t = query[q].split(" ")
            q_data = []
            for i in q_data_t:
                if i != '' and i != 'and':
                    q_data.append(i)

            q_lang = q_data[0]
            q_part = q_data[1]
            q_career = q_data[2]
            q_soulfood = q_data[3]
            q_score = q_data[4]

            if q_lang == i_lang or q_lang == "-":
                if q_part == i_part or q_part == "-":
                    if q_career == i_career or q_career == "-":
                        if q_soulfood == i_soulfood or q_soulfood == "-":
                            if int(i_score) >= int(q_score):
                                answer[q] += 1

    return answer


'''
효율성에서 0점.. 더 최적화 할 수 있는 방안을 고민해야한다..
'''