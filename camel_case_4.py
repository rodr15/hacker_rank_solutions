


import sys


def concat(tipe,words):
    output_word = words[0]
    
    for index in range(1,len(words)):
        output_word += words[index].capitalize()

    if( tipe == 'M' ): output_word += '()'
    if( tipe == 'C' ):output_word = output_word[0].upper() + output_word[1:]
    else: output_word = output_word[0].lower() + output_word[1:]

    return output_word


def split(tipe,words):
    output_word = ''
    for word in words:
        for index,letter in enumerate(word):
            if ( letter == letter.upper() and index != 0): 
                output_word += ' '
            output_word +=  letter
            

    return output_word.lower()


if __name__ == '__main__':
    operation,tipe,words  = 'S;M;sweatTea()'.split(';');
    
    words = words.replace('()','')
    words = words.split(' ')
    

    if( operation == 'S' ):
        print(split(tipe,words))
    if( operation == 'C' ):
        print(concat(tipe,words))
            