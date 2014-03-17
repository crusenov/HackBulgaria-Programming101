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

def prime_number_of_divisors( n ):
	count = 0
	i = 1 
	while i <= n:
		if n % i == 0:
			count += 1
		i += 1
	if is_prime(count):
		return True
	else:
		return False

