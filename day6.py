with open('input.txt') as inp:
    lines = inp.readlines()
    ans, people, sum = [0] * 26, 0, 0
    for line in lines:
        line = line.strip()
        if line == "":
            for i in range(26):
                if ans[i] == people:
                    sum += 1
            people = 0
            ans = [0] * 26
        else:
            for k in line:
                ans[ord(k) - ord('a')] += 1
            people += 1
    print(sum)