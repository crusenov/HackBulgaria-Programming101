import sys
from random import randint

def generate_numbers(*args):
	if len(sys.argv) == 3:
		fname  = sys.argv[1]
		n = int(sys.argv[2])
		file = open(fname, "w")
		for i in range(0, n):
			r = randint(1, 1000)
			file.write(" ".join(str(r)))
		file.close()
	elif len(sys.argv) > 3:
		print ("Too much arguments!")
	elif len(sys.argv) < 3:
		print ("No arguments given!")
	file.close()

def main():
	generate_numbers(sys.argv)


if __name__ == '__main__':
	main()