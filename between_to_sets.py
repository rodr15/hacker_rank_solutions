


def getTotalX(a, b):
    # Write your code here
    num_between_a = []
    num_between_b = []
    append= True
    
    for i in range(1,101):
        for elemenet_a in a:
            if(i % elemenet_a != 0):
                append = False
                break;
        if append: num_between_a.append(i)
        append = True
        
        for elemenet_b in b:
            if(elemenet_b % i != 0):
                append = False
                break;
        if append: num_between_b.append(i)
        append = True


    lista = [x for x in num_between_a if x in num_between_b]

    print(num_between_a)
    print(num_between_b)
    print(lista)
    return len(lista)

if __name__ == '__main__':
    a = [1]
    b = [100]
    print(getTotalX(a,b))

    # 3.9.4 (default, Apr 10 2021, 15:39:19) 