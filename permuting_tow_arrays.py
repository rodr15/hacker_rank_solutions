def twoArrays(k, A, B):
    
    A.sort()
    B.sort(reverse = True)
    for i in range(len(A)):
        
        if ( A[i] + B[i] < k): return 'NO'
    return 'YES'


if __name__ == '__main__':

    k = 5
    A = [1, 2, 2, 1]
    B = [3, 3, 3, 4]
    print(twoArrays(k,A,B))