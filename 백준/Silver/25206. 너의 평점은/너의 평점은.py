score = {
    'A+' : 4.5,
    'A0' : 4.0,
    'B+' : 3.5,
    'B0' : 3.0,
    'C+' : 2.5,
    'C0' : 2.0,
    'D+' : 1.5,
    'D0' : 1.0,
    'F' : 0.0,
}

hakjeom = []
jeongong = []
jeongongscore = []
finalscore = []
sumV = 0
answer = 0
lst = [list(map(str, input().split())) for _ in range(20)]
# pprint(lst)

for i in range(len(lst)):
    if lst[i][2] != "P":
        hakjeom.append(lst[i][1])
        jeongong.append(lst[i][2])

for i in jeongong:
    if i in score.keys():
        jeongongscore.append(score[i])

# pprint(len(jeongongscore))

for i in range(len(hakjeom)):
    for j in range(len(jeongongscore)):
        if i == j:
            finalscore.append(float(hakjeom[i]) * float(jeongongscore[j]))
for i in range(len(hakjeom)):
    sumV += float(hakjeom[i])
# print(sum(finalscore))
# print(sumV)
answer = round(sum(finalscore) / sumV, 6)
print(answer)
