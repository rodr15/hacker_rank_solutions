def maximumPerimeterTriangle(sticks):
    # Write your code here
    sticks.sort()
    posibilities = []
    for j in range( len( sticks ) ):
        for i in range( len( sticks ) - 2 ):
            a = sticks[ i ]
            b = sticks[ i + 1 ]
            c = max(sticks)
            if( a + b  > c ):
                posibilities.append((a,b,c))
        sticks.remove(max(sticks))
    
    posibilities.sort()
    
    if ( len( posibilities ) == 0 ):
        return -1
    
    return max(posibilities)
    
        

if __name__ == '__main__':
    # sticks = [ 1, 2, 3, 4, 5, 10 ]
    # sticks = [ 1, 1, 1 , 3, 3 ]
    sticks = [1 ,2 ,3]
    print( maximumPerimeterTriangle( sticks ) )