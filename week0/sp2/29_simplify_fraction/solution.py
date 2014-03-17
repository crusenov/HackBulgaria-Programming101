from fractions import gcd

def simplify_fraction(fraction):
	x = gcd(fraction[0], fraction[1])
	p = fraction[0] // x
	q = fraction[1] // x
	arr = (p, q)
	return arr

def main():
	print(simplify_fraction((3,9)))
	print(simplify_fraction((1,7)))
	print(simplify_fraction((4,10)))
	print(simplify_fraction((63,462)))

if __name__ == '__main__':
	main()