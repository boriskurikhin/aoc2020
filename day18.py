'''
    recursion
    these questions are always tough 
'''
with open('input.txt') as ___:
    lines =  ___.readlines()

    def bracketIndex(exp, i):
        b = 1
        i += 1
        while i < len(exp):
            if exp[i] == ')':
                b -= 1
                if b == 0:
                    return numberIndex(exp, i)
            elif exp[i] == '(':
                b += 1
            i += 1
        raise Exception('something broke')

    def numberIndex(exp, i):
        i = i + 1
        while i < len(exp):
            if exp[i].isnumeric() or exp[i] in ['(', ')']:
                return i
            i += 1
        return i

    def calc (exp, i):
        if i == len(exp):
            return 0
        v = 0
        if exp[i] == '(':
            v = calc(exp, i + 1)
        else:
            v = int(exp[i])
            i = numberIndex(exp, i)
        while i < len(exp):
            sign = exp[i - 2]
            if exp[i] == '(':
                if sign == '*': v *= calc(exp, i+1)
                elif sign == '+': v += calc(exp, i+1)
                i = bracketIndex(exp, i)
            elif exp[i].isnumeric():
                if sign == '*': v *= int(exp[i])
                else: v += int(exp[i])
                i = numberIndex(exp, i)
            else:
                break
        return v
    
    s = 0
    for l in lines:
        s += calc(l.strip(), 0)
    print(s)
