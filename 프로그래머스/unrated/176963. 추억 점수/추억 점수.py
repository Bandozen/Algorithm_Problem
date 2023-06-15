def solution(name, yearning, photo):
    score = 0
    name_dic = {}
    score_list = []
    for i in range(len(name)):
        name_dic[name[i]] = yearning[i]
    for i in range(len(photo)):
        for j in range(len(photo[i])):
            if photo[i][j] in name_dic:
                score += name_dic[photo[i][j]]
        score_list.append(score)
        score = 0
    return score_list