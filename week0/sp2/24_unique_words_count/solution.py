def unique_words_count(arr):
	c = 0
	new = []
	for i in range(0, len(arr)):
	    if arr[i] not in new:
	        new.append(arr[i])
	return len(new)

def main():
	print (unique_words_count(["apple", "banana", "apple", "pie"]))
	print (unique_words_count(["python", "python", "python", "ruby"]))
	print (unique_words_count(["HELLO!"] * 10))
if __name__ == '__main__':
	main()