def sum_of_divisors( n ):
	sum = 0
	i = 1
	while i <= n:
		if n % i == 0: 
			sum += i
		i += 1

	return sum	

