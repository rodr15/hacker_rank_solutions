
def flippingMatrix(matrix):
    
    l = len(matrix) 

    mayor = []

    for x in range(l / 2):
        for y in range(l / 2):
            mayor.append(  max(     matrix[x][y],
                                    matrix[x][ l - 1 - y],
                                    matrix[l - 1 - x][y],
                                    matrix[l - 1 - x][l - 1 - y]  ))
            
    return sum(mayor)
        
        

if __name__ == '__main__':
    matrix = [  [112, 42 , 83 , 119], 
                [56 , 125, 56 , 49 ], 
                [15 , 78 , 101, 43 ], 
                [62 , 98 , 114, 108]      ]
    print(flippingMatrix(matrix))

                # [x1, x2 , x3 , x3, x2 , x1], 
                # [56 , 125, 56 , 49 , 2 , 3], 
                # [15 , 78 , 101, 43 , 2 , 3], 
                # [62 , 98 , 114, 108, 2 , 3],  
                # [62 , 98 , 114, 108, 2 , 3],  
                # [x1 , x2 , x3, x3, x2 , x1],  