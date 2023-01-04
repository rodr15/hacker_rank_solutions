def findZigZagSequence(a, n):
    a.sort()
    mid = int((n + 1)/2) - 1
    a[mid], a[n-1] = a[n-1], a[mid]

    st = mid + 1
    ed = n - 2
    print('Antes While',a)
    while(st <= ed ):
        print('{} <-> {}'.format(a[st], a[ed]))
        a[st], a[ed] = a[ed], a[st]
        print('Despues del cambio',a)
        st = st + 1
        ed = ed - 1
    
    
    for i in range (n):
        if i == n-1:
            print(a[i])
        else:
            print(a[i])
    return

if __name__ == '__main__':
    arr = [1,2,3,4,5,6,7]
    findZigZagSequence(arr,len(arr))
    # 1 2 3 7 6 5 4