def count_words(arr):
	d = {}
	for i in arr:
		if i in d:
			d[i] += 1
		else: 
			d[i] = 1
	return d


def main():
	print(count_words(["apple", "banana", "apple", "pie"]))
	print(count_words(["python", "python", "python", "ruby"]))

if __name__ == '__main__':
	main()
		



		
		

