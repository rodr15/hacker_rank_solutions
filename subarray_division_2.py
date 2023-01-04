def birthday(s, d, m):
    way = 0
    suma = 0
    for index in range(len(s)):
        
        if ( sum( s[ index : index + m ] ) ==  d ):
            way += 1



    return way
    

if __name__ == '__main__':
    s = [2,2,1,3,2]
    d = 4
    m = 2
    print(birthday(s,d,m))