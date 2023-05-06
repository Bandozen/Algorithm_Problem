def solution(s):
    while s.isdigit() == False:
        if s.find('one') != -1:
            s = s.replace('one', '1')
        elif s.find('two') != -1:
            s = s.replace('two', '2')
        elif s.find('three') != -1:
            s = s.replace('three', '3')
        elif s.find('four') != -1:
            s = s.replace('four', '4')
        elif s.find('five') != -1:
            s = s.replace('five', '5')
        elif s.find('six') != -1:
            s = s.replace('six', '6')
        elif s.find('seven') != -1:
            s = s.replace('seven', '7')
        elif s.find('eight') != -1:
            s = s.replace('eight', '8')
        elif s.find('nine') != -1:
            s = s.replace('nine', '9')
        elif s.find('zero') != -1:
            s = s.replace('zero', '0')
        else:
            None
    return int(s)