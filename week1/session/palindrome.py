from bwsi_grader.python.palindrome import grader

def student_func(x) :
    x = x.lower().replace(" ", "")
    rev = x[::-1]
    if x == rev : 
        return True
    else :
        return False
        
grader(student_func)
