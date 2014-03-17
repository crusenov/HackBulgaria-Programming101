def calculate_coins(num):
    d = {}
    coins = [100, 50, 20, 10, 5, 2, 1]
    num *= 100
    for i in coins:
        count = 0
        while num % i >= 0 and num // i != 0:
            count += int(num // i)
            num %= i
        d[i] = count
    return d




def main():
    print(calculate_coins(0.53))
    print(calculate_coins(8.94))


if __name__ == '__main__':
    main()
