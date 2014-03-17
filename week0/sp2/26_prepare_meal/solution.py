def prepare_meal(number):
	flag = 0
	count = 0
	n5 = number
	n3 = number
	if n5 % 5 == 0:
		flag = 1
		n5 //= 5
	else:
		flag = 0
	while n3 % 3 == 0:
		count += 1
		n3 //= 3
	if number % 3 != 0:
		count = -1
	if flag == 1 and count == -1:
		return "eggs"
	elif flag == 1 and count > -1:
		return "spam " * count + "and eggs"
	elif flag == 0 and count > 1:
		string = "spam " * count
		if string[len(string) - 1] == " ":
			return string[:len(string)-1]
	elif flag == 0 and count == 1:
		return "spam" * count
	else:
		return ""

def main():
	print(prepare_meal(5))
	print(prepare_meal(3))
	print(prepare_meal(27))
	print(prepare_meal(15))
	print(prepare_meal(45))
	print(prepare_meal(7))

if __name__ == '__main__':
	main()

