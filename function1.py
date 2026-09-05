# Calculate the total marks
def Calculate_total(marks):
    total = sum(marks)
    return total

#Calculate percentage
def Calculate_percentage(total,subject=5):
    percentage = total/subject
    return percentage
# Find the grade

def find_gread(percentage):
    if percentage >= 75:
        return "A"
    elif percentage >= 60:
        return "B"
    elif percentage >= 50:
        return "C"
    elif percentage >= 35:
        return "D"
    else:
        return "Fail"
# Function 4:Callback Function
def print_result(name,marks,callback):
    total = Calculate_total(marks)
    percentage = Calculate_percentage(total)
    grade = find_gread(percentage)
    print("Name :",name)
    print("marks:",marks)
    print("total:",total)
    print("percentage:",percentage)
    print("grade:",grade)

# Calling a function reverse as a parameter 
    callback(name,percentage,grade)

# callback function
def Final_message(name,percentage,grade):
    if grade == "Fail":
        print("has failed.",name)
    else:
        print("has paased with grade:",grade)

# function call
marks = [80,75,90,85,70]
print_result("pranavi",marks,Final_message)
