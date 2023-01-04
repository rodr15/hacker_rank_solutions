def _do_number(lista):
    number = 0
    for elev,num in enumerate(lista[::-1]):
        number += num * (10**elev)
    return number



def separateNumbers(s):
    if len(s) <= 1:
        print('NO')
        return

    s = [int(x) for x in s]
    s = _separate(s)

    last_num = s[0]
    print(s)
    for num in s :
        if last_num - num != 1:
            print('NO')
            return
    
    print('YES {}'.format(s[0]))
            

             
            
            
def _separate(s):

    out = []

    index = 0
    last_index = 1
    num = s[0]
    while index < len(s):
        
        const = 1
        while _do_number(s[index:index + const ]) - num < 1:
            
            num = _do_number(s[index:index + const])
            const += 1
            if index + const > len(s): break
        print(num)
        index += const + 1
    
    return [1]


if __name__ == '__main__':
    # inputs = ["7","1234","91011","99100","101103","010203","13","1"]
    inputs = ["99100"]
     
    for i in inputs:
        print('-' * 25)
        print(i)
        separateNumbers(i)
        
    