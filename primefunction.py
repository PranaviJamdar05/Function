def is_prime(number):
    if number < 2:
        return False

    for i in range(2,number):
        if number % i == 0:
            return False

    return True

def filter_number(numbers,condition):
    result = []
    for number in numbers:
        if condition(number):
            result.append(number)

    return result


numbers = [2,4,5,7,8,9,12,23,15]
prime_number = filter_number(numbers,is_prime)
print("Prime number:",prime_number)

        
