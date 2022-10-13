'''
Program: function_keyword_and_arbitrary_arguments.py
Author: Joshua M McGinley
Last Date Modified: 10/12/2022

Complete the average_scores() functions using arbitrary argument lists and keyword arguments and returning a
string in the following format (for example, you will have your own):

Note: I left the above for historical purposes, the only calculation should be on the GPA; you do not need to
include a current assignment average (the current average = 30.0 part) as our assigment doesn't take test scores in.
The keywords will include student name, course name, current gpa. The example above used name, gpa, and course.
You can select your own.
In main, make at least 3 function calls, each with a different number of scores and different keyword arguments.
This is worth 5 points.

'''

def average_scores(*args, **kwargs):
    total = 0
    count = 0
    for num in args:
        total += num
        count = count + 1
    for key, value in kwargs.items():
        print('%s==%s'% (key,value))
    average = total / count
    return (average, key, value)

if __name__=='__main__':
    print(average_scores(4,3,2,4, first_name='Michelle', last_name ='Ruse', major='World_domination'))
