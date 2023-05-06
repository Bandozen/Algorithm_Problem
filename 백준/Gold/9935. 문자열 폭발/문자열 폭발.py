txt = input()
explosion = input()

stack = []
ex_len = len(explosion)

for i in range(len(txt)):
    stack.append(txt[i])
    if ''.join(stack[-ex_len:]) == explosion:
        for _ in range(ex_len):
            stack.pop()

if stack:
    print(''.join(stack))
else:
    print('FRULA')
