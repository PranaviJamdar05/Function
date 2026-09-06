def Addition(marks):
    sum = 0

    for mark in marks:
        sum = sum + mark

    return sum
def Maximum(marks):
    max_mark = marks[0]

    for mark in marks:
        if mark > max_mark:
            max_mark = mark

    return max_mark
def Minimum(marks):
    min_mark = marks[0]

    for mark in marks:
        if mark < min_mark:
            min_mark = mark

    return min_mark

def analyze(marks,function):
    result = function(marks)
    print("marks:",marks)
    print("Result:",result)

marks = [75,89,64,92,81]

analyze (marks,Addition)
analyze(marks,Maximum)
analyze(marks,Minimum)
