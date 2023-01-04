def gradingStudents(grades):
    # Write your code here
    base = 5 
    for index,grade in enumerate(grades):
        if( grade > 37):
            next_multiple = base * round(grade / base)
            if(next_multiple < grade): next_multiple += base
            if ( next_multiple - grade < 3): 
                grades[index] = int(next_multiple)
            

    return grades
if __name__ == '__main__':
    print(gradingStudents([73 ,67 , 38 ,33]))