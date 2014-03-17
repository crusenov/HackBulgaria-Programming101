def is_number_balanced(n):
    x = str(n)
    sumR = 0
    sumL = 0
    if len(x) % 2 == 0:
        length = len(x) // 2
        for i in range(0, length):
            sumL += int(x[i])
        for j in range(length, len(x)):
            sumR += int(x[j])
    else:
        length = (len(x) // 2) + 1
        for i in range(0, length-1):
            sumL += int(x[i])
        for j in range(length, len(x)):
            sumR += int(x[j])
    if sumR == sumL or len(x) == 1:
        return True
    else:
        return False

def main():
    print( is_number_balanced(121))
    print(is_number_balanced(4518))
    print( is_number_balanced(1238033))

if __name__ == '__main__':
    main()
