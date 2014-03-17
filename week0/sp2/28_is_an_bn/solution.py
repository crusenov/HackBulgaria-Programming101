def is_an_bn(word):
	c = 0
	for i in range(len(word)-1):
		if word[i] == "a":
			c += 1
			if word[i+1] == "b":
				for j in range(c, len(word)):
					if word[j] == "b":
						c -= 1
	if c == 0:
		return True
	else:
		return False



def main():
	print(is_an_bn(""))
	print(is_an_bn("rado"))
	print(is_an_bn("aaabb"))
	print(is_an_bn("aaabbb"))
	print(is_an_bn("bbbaaa"))

if __name__ == '__main__':
	main()
