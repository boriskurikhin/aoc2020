# bitmask math
# had some difficulty understanding the question today
# but we solved it at last

with open('input.txt') as ___:
    lines = list(map(lambda x: x.strip(), ___.readlines()))
    bitMask = 0
    memory = {}
    for i in range(len(lines)):
        L = lines[i]
        if L.startswith('mask'):
            m = L[7:][::-1]
            bitMask = m
        else:
            address = int(L[L.index('[') + 1:L.index(']')])
            va = L.split(' = ')
            value = int(va[1])
            quantum = []

            # apply mask            
            for i in range(len(bitMask)):
                if bitMask[i] == 'X': quantum.append(i) 
                else: address |= (int(bitMask[i]) << i)

            # powerset
            N = 2 ** len(quantum)
            for isSet in range(N):
                for k in range(len(quantum)):
                    if isSet & (1 << k): address |= (1 << quantum[k])
                    else: address &= ~(1 << quantum[k])
                memory[address] = value

    print(sum(memory.values()))