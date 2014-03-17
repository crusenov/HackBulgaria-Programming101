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
    

def contains_digits(number, digit):
    flag = 0
    for i in digit:
        if contains_digit(number, i):
            flag = 1
        else:
            flag = 0
    if flag == 1 or len(digit) == 0:
        return True
    else: 
        return False

def main():
    print(contains_digits(456, []))
    print(contains_digits(402123, [0, 3, 4]))

if __name__ == '__main__':
    main()