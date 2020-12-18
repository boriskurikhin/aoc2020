
'''
    brain so big it doesn't fit in my head
'''
class CoolInteger(int):
    def __init__(self, value):
        self.value = value
    def __add__(self, other):
        return CoolInteger(self.value * other.value)
    def __mul__(self, other):
        return CoolInteger(self.value + other.value)
    def __repr__(self):
        return f'CoolInteger({ self.value })'
        
with open('input.txt') as ___:
    lines =  ___.readlines()
    import re
    ans = 0
    for l in lines:
        rep = re.sub(r'(\d)', r'CoolInteger(\1)', l) \
            .replace('+', '!') \
            .replace('*', '+') \
            .replace('!', '*')
        ans += eval(rep)
    print(ans)
        