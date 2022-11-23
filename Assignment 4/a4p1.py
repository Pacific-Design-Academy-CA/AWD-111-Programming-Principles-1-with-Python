#!/usr/bin/env python3


''' Grading
Range - Letter Grade - Point grades
00-50 - F - 0
51-60 - D - 1
61-70 - C - 2
71-80 - B - 3
81-90 - A - 4
91-100 - A+ - 5 
if a student get's the following grades in 4 subjects for Fall 2022:
    Maths: 82 -> A -> 4
    Physics: 65 -> C -> 2
    Chemistry: 75 -> B -> 3
    English: 77 -> B -> 3
The student's sessional gpa would be:
Total points: 4+2+3+3 = 12
Sessional gpa: Total points/Total number of course = 12/4 = 3
The sessional letter grade for that student is B

**if the GPA of a student is in floating point please use the
int() function to convert to an integer**

'''

def dataExtraction(fileName):
    ''' input : fileName'''
    ''' The file student info contains the name-age-school-grades of students'''
    ''' Extract the info for each students from the file, store it in 
    a list of dictionaries '''
    ''' where each dictionary should have the following identical key '''
    ''' student1 = {"name":"jess", 
                    "age":27,
                    "school":"PDA",
                    "grades":[78,82,65,55]}'''
    ''' the list of dictionary would look like this '''
    ''' list_dicts = [student1, student2, student3,..] '''
    ''' output: return list_dicts '''    
    
    pass
    # return list_dicts        

   


def dataPrinting(list_dicts):
    ''' Input: list of dictionaries with the student info'''
    ''' Output: print each student info in the following format '''
    '''Student-01 jess 27 PDA 78-82-65-55'''
    '''Student-02 mindy 22 PDA 80-55-75-77'''
    '''so on..'''
    ''' as you can see each info is sepearated by a space
    and each student info will be printed in a newline'''      

def longestStudentName(list_dicts):
    '''Input: List of dictionaries with the student info '''
    ''' Output: Print the student with the longest name '''
    ''' **if there are multiple students with the same length for
    the longest name, print together separated by space/" " '''
    pass


def calculateHighestSessionalGPA(list_dicts):
    '''Input: List of dictionaries with the student info '''
    '''Output: Print the name&GPA of the student with the highest 
    sessional GPA'''
    '''Format: remy:4'''
    ''' If there are multiple students with the same highest sessional
    GPA, print names&grades of all students separated by space in alphabetical order'''
    ''' Format- audrey:4 remy:4 tim:4'''
    pass

if __name__ == '__main__':
    
    #step 1
    #read the grading carefully
    #okay now extract data from the file "student-info.txt"

    list_dicts = dataExtraction("student-info.txt")

    #step 2
    #data printing with list_dicts as parameter
    dataPrinting(list_dicts)

    #step 3
    #longest student name from list of dictionaries with student info
    longestStudentName(list_dicts)


    #step 4
    #calculate highest sessional GPA using list of dictionaries with student info
    calculateHighestSessionalGPA(list_dicts)
