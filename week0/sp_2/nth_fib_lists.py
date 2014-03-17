def nth_fib_lists(listA, listB, n):
	if n == 1:
		return listA
	if n == 2:
		return listB
	return (listB, listA+listB, n-1)


def main():
	print(nth_fib_lists([1], [2], 1))
	print(nth_fib_lists([1], [2], 2))
	print(nth_fib_lists([1, 2], [1, 3], 3))
	print(nth_fib_lists([], [1, 2, 3], 4))
	print(nth_fib_lists([], [], 100))


if __name__ == '__main__':
	main()