def is_even(num):
    return num % 2 == 0


def is_odd(num):
    return num % 2 != 0


def check_num(numbers, condition):

    for num in numbers:

        if condition(num):
            print(num)


num = [10, 102, 475, 29, 90, 67]

print("Even number:")
check_num(num, is_even)

print("Odd number:")
check_num(num, is_odd)
