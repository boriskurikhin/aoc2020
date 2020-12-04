with open('input.txt') as inp:
    lines = inp.readlines()
    checks = set(['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid', 'cid'])
    have = set()
    result = 0

    '''
    I can't believe that I kept finding
    the number of invalid passwords...
    smh

    this was a really annoying one...
    '''

    import re

    for line in lines:
        line = line.strip()
        if len(line) == 0:
            both = checks & have
            if 'cid' in both:
                both.remove('cid')
            if len(both) >= 7:
                result += 1
            have = set()
            continue
        attrs = line.split(' ')
        for attr in attrs:
            props = attr.split(':')
            
            key = props[0]
            val = props[1]

            if key == 'byr':
                if int(val) < 1920 or int(val) > 2002:
                    continue
            elif key == 'iyr':
                if int(val) < 2010 or int(val) > 2020:
                    continue
            elif key == 'eyr':
                if int(val) < 2020 or int(val) > 2030:
                    continue
            elif key == 'hgt':
                if val[::-1][:2] not in ['mc', 'ni']:
                    continue
                if val[::-1][:2] == 'mc' and (int(val[0:len(val)-2]) < 150 or int(val[0:len(val)-2]) > 193): continue
                if val[::-1][:2] == 'ni' and (int(val[0:len(val)-2]) < 59 or int(val[0:len(val)-2]) > 76): continue
            elif key == 'hcl':
                if not re.match("^(#[0-9a-f]{6})$", val): 
                    continue
            elif key == 'ecl':
                if not val in ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']: continue 
            elif key == 'pid':
                if not re.match("^([0-9]{9})$", val): 
                    continue
            # if valid
            have.add(key)
    print(result)
    
