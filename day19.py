with open('input.txt') as ___:
    lines =  ___.readlines()
    rules = {}
    i = 0
    while i < len(lines):
        inp = lines[i].strip()
        if len(inp) == 0: break
        inp = inp.split(': ')
        ruleId = int(inp[0]) 
        if inp[1][0] == '"':
            rules[ruleId] = inp[1][1:-1]
        else:
            parse = inp[1].split(' | ')
            rules[ruleId] = []
            for p in parse:
                rules[ruleId].append(tuple(map(lambda x: int(x), p.split(' '))))
        i += 1
    i += 1
    ans = 0

    print(rules)

    from copy import deepcopy
    def go(text, ruleId):
        if type(rules[ruleId]) == str:
            term = rules[ruleId]
            return len(term) if text.startswith(term) else -1
        
        bestAns = 0
        for option in rules[ruleId]:
            ans = 0
            for n in option:
                parsed = go(text[ans:], n)
                if parsed == -1:
                    break
                ans += parsed
            bestAns = max(ans, bestAns)
        return bestAns
    f = 0
    while i < len(lines):
        inp = lines[i].strip()
        f += 1 if go(inp, 0) == len(inp) else 0
        i += 1
    print(f)

  