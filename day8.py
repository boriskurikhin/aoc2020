'''
    didn't do that well today
    misunderstood part 2, thought we
    had to return the index that caused the loop
    ... 
    spent 40 min debugging why it didn't work
    ehhhhh
'''

with open('input.txt') as ___:
    lines = list(map(lambda x: x.strip(), ___.readlines()))

    def simulate():
        visited = set()
    
        p = 0
        acc = 0
        last = 0

        while True:
            if p >= len(lines):
                print(acc)
                return 

            inst = lines[p].split(' ')
            command = inst[0]
            sign = inst[1][0]
            value = int(inst[1][1:])

            if p in visited:
                return

            visited.add(p)
            
            if command == 'nop':
                last = p
                p += 1
            elif command == 'acc':
                if sign == '-': acc -= value
                else: acc += value
                p += 1
            else:
                last = p
                if sign == '-': p = p - value
                else: p = p + value
    
    for j in range(len(lines)):
        if 'jmp' in lines[j]:
            lines[j] = lines[j].replace('jmp', 'nop')
            simulate()
            lines[j] = lines[j].replace('nop', 'jmp')
        if 'nop' in lines[j]:
            lines[j] = lines[j].replace('nop', 'jmp')
            simulate()
            lines[j] = lines[j].replace('jmp', 'nop')

        