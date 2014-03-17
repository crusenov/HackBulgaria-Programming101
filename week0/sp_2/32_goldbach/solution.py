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

def goldbach(n):
	primes = [x for x in range(1, n) if is_prime(x)]
	final = sorted([(p,q) for p in primes for q in primes if p+q == n and p <= q])
	return final

def main():
	print(goldbach(4))
	print(goldbach(6))
	print(goldbach(8))
	print(goldbach(10))
	print(goldbach(100))

if __name__ == '__main__':
	main()