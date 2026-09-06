def add(a,b):
    return a + b
def sub(a,b):
    return a - b
def mul(a,b):
    return a * b
def div(a,b):
    return a / b
def calculation(a,b,opration): # callback concept
    result = opration(a,b)
    print("Result is:",result)

calculation(10,20,add)
calculation(10,20,sub)
calculation(10,20,mul)
calculation(10,20,div)

