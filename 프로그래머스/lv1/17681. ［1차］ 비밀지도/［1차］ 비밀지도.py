def solution(n, arr1, arr2):
    arr1_bin = []
    arr2_bin = []
    answer = [''] * n
    
    for i in range(len(arr1)):
        bin_1 = bin(arr1[i]).replace('0b', '')
        if len(bin_1) != n:
            bin_1 = (n - len(bin_1)) * '0' + bin_1
        arr1_bin.append(bin_1)
    
    for i in range(len(arr2)):
        bin_2 = bin(arr2[i]).replace('0b', '')
        if len(bin_2) != n:
            bin_2 = (n - len(bin_2)) * '0' + bin_2
        arr2_bin.append(bin_2)
    
    for i in range(len(answer)):
        security = ''
        for j in range(len(arr1_bin)):
            if arr1_bin[i][j] == '1' or arr2_bin[i][j] == '1':
                security += '#'
            else:
                security += ' '
        answer.append(security)
    
    for i in range(n):
        answer.remove('')
            
    return answer