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

def main():
	print(is_prime(-10))

if __name__ == '__main__':
	main()