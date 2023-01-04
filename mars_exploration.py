def marsExploration(s):
    # Write your code here
    
    changes = 0
    # sos = 'SOS'
    # for index in range((len(s) / 3)):
    #     sos_message = s[index * 3 : (index + 1) * 3 ]
    #     if( sos_message != sos):
    #         for index_message in range(len(sos_message)):
    #             if(sos_message[index_message] != sos[index_message]):
    #                 changes += 1

    r = len(s) / 3
    target = 'SOS' * r
    for i,j in zip(s,target):
        if ( i != j ): changes += 1

    return changes

if __name__ == '__main__':
    s = 'SOSSPSSQSSOR'
    print(marsExploration(s))