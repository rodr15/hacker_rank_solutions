def divisibleSumPairs(n, k, ar):
    num_tuples = 0
    
    for i in range(len(ar)):
        for j in range(len(ar)):
            if( i != j):
                if( (ar[i] + ar [j]) % k == 0 ):
                    num_tuples += 1

    return num_tuples / 2

if __name__ == '__main__':
    print(divisibleSumPairs(6,3,ar = [1,3,2,6,1,2]))