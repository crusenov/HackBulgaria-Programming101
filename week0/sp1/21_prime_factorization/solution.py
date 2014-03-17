def is_prime( n ):
	n = abs( n )
	flag = 0
	i = 2
	if n == 1:
		return False
	if n == 2:
		return True
	while i <= n/2:
		if n % i == 0:
			flag = 1
		i += 1
	if flag == 0:
		return True
	else: 
		return False

def prime_factorization(n):
	arr = []
	for i in range(2, n+1):
		count = 0
		while n % i == 0:
			count += 1
			n //= i
			if n % i != 0:
				new = (i, count)
				arr.append(new)
	return arr

def main():
	print(prime_factorization(10))
	print(prime_factorization(14))
	print(prime_factorization(356))
	print(prime_factorization(89))
	print(prime_factorization(1000))

if __name__ == '__main__':
	main()



