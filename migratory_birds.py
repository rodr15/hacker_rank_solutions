from operator import indexOf


def migratoryBirds(arr):
    # Write your code here
    unique = set(arr)
    rep = [0] * ( max( unique ) + 1 )
    
    for bird in arr:
        rep[bird] += 1
    
    return rep.index(max(rep))
    

        

if __name__ == '__main__':
    ar = [2,1,2,1,3]
    print(migratoryBirds(ar))