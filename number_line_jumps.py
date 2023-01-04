def kangaroo(x1, v1, x2, v2):
    # Write your code here

    for i in range(10000):
        x1 += v1
        x2 += v2
        if x1 == x2: return 'YES';
        if(i == 10000 - 1): return 'NO';

if __name__ == '__main__':
    x1 = 0
    v1 = 2
    x2 = 5
    v2 = 3
    print(kangaroo(x1,v1,x2,v2))