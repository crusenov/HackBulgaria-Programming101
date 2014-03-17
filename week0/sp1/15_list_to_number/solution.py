def list_to_number(digits):
    num = 0
    for i in digits:
        num += i
        num *= 10
    return num // 10