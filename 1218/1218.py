def find_case(x):
    dict_a = {
    '()' : 0,
    '[]' : 0,
    '{}' : 0,
    '<>' : 0
    }

    for char in x:
        if dict_a['()'] == -1 or  dict_a['[]'] == -1 or  dict_a['{}'] == -1 or dict_a['<>'] == -1:
            return 0

        if char == '(':
            dict_a['()'] +=1
        elif char == '[':
            dict_a['[]'] +=1
        elif char == '{':
            dict_a['{}'] +=1
        elif char == '<':
            dict_a['<>'] +=1
        
        if char == ')':
            dict_a['()'] -=1
        elif char == ']':
            dict_a['[]'] -=1
        elif char == '}':
            dict_a['{}'] -=1
        elif char == '>':
            dict_a['<>'] -=1
        
    return 1

for i in range(1, 11):
    n = int(input())
    x = str(input())
    print(f'#{i} {find_case(x)}')
