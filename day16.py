'''
    Yeah...this one is a bit.
    Not great lol. But it works, quite fast.
'''
def check_ticket(ticket, rules):
    for name in rules:
        a = rules[name][0]
        b = rules[name][1]

        if (ticket >= a[0] and ticket <= a[1]) or (ticket >= b[0] and ticket <= b[1]):
            return True
    return False

import copy

memo = set()

def checkWinner(options, N):
    solutions = set()
    for name in options:
        if len(options[name]) != 1:
            return False
        solutions.add(options[name][0])
    return len(solutions) == N

def existsEmpty(options):
    for name in options:
        if len(options[name]) == 0:
            return True
    return False

def solveOptimization(options, N, solutionsFound, z, myTicket):

    # if existsEmpty(options):
    #     return

    if solutionsFound == N:
        # print('winner found', z)
        ans = 1
        for tup in z:
            name, col = tup
            if name.startswith('departure'):
                ans *= myTicket[col]
        print(ans)
        exit(0)

    newOptions = copy.deepcopy(options)
    for name in dict(sorted(options.items(), key=lambda item: len(item))):
        candidates = options[name]
        for candidate in candidates:
            
            newZ = copy.deepcopy(z)
            newZ.append((name, candidate))

            # remove this option
            O = copy.deepcopy(options)
            del O[name]
            
            for n in O:
                if candidate in O[n]:
                    O[n].remove(candidate)

            solveOptimization(O, N, solutionsFound + 1, newZ, myTicket)

def candidates(tickets, r, options):
    a = rules[r][0]
    b = rules[r][1]
    
    options[r] = []
    N = len(tickets[0])

    for colIndex in range(0, N):
        isCandidate = True
        # if any one element is bad, this is not a candidate
        for rowIndex in range(0, len(tickets)):
            t = tickets[rowIndex][colIndex]
            if t == 'ignore': 
                continue
            if not ((t >= a[0] and t <= a[1]) or (t >= b[0] and t <= b[1])):
                isCandidate = False
                break
        # if is candidate
        if isCandidate:
            options[r].append(colIndex)
            
with open('input.txt') as ___:
    lines =  ___.readlines()
    i = 0

    rules = {}

    # parse rules
    while i < len(lines):
        if lines[i] == '\n': break

        # create rule mapping
        line = lines[i].split(': ')
        rules[line[0]] = []

        bounds = line[1].split(" or ")
        ab = bounds[0].split('-')
        rules[line[0]].append((int(ab[0]), int(ab[1])))
        bb = bounds[1].split('-')
        rules[line[0]].append((int(bb[0]), int(bb[1])))

        i += 1
    i += 2
    myTicket = list(map(lambda x: int(x), lines[i].strip().split(',')))
    
    allTickets = []
    i += 3
    ans1 = 0
    while i < len(lines):
        ticks = list(map(lambda x: int(x), lines[i].strip().split(',')))
        goodBounds = []
        toAdd = []
        for t in ticks: 
            if not check_ticket(t, rules): 
                ans1 += t
                toAdd.append('ignore')
            else: toAdd.append(t)

        allTickets.append(toAdd)
        i += 1
    
    allTickets.append(myTicket)
    options = {}

    # we need to figure out column candidates for each rule
    for r in rules:
        candidates(allTickets, r, options)

    sortedOpts = {}
    from heapq import heappop, heappush
    heap, keys = [], options.keys()

    for i in keys:
        heappush(heap, (len(options[i]), i, options[i]) )

    while len(heap):
        L, name, arr = heappop(heap)
        sortedOpts[name] = arr

    solveOptimization(sortedOpts, len(keys), 0, [], myTicket)
    


    