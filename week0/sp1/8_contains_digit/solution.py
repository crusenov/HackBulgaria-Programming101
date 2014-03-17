def contains_digit(number, digit):
    flag = 0
    while number:
        if digit == number % 10:
            flag = 1
        number = number // 10
    if flag == 1:
        return True
    else: 
        return False