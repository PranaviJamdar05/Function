def square(number):
    return number * number
def Cube(number):
    return number * number* number
def double(number):
    return number*2
def process(numbers,function): # higher order function
    result = []
    for number in numbers:
        Value = function(number)
        result.append(Value)

    return result

numbers = [1,2,3,4,5,6,7,8,9]

print("Square:",process(numbers,square))  #Call back function
print("Cube:",process(numbers,Cube))
print("double:",process(numbers,double))

