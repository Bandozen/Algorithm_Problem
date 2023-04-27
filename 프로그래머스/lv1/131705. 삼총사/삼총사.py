def solution(number):
    answer = 0
    for i in range(len(number)-2):
        a=number[i]
        for j in range(i+1,len(number)-1):
            b=number[j]
            for k in range(j+1,len(number)):
                c=number[k]
                if a+b+c==0:
                    answer+=1

    return answer