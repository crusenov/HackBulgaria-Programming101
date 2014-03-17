def sudoku_solved(sudoku):
	res = [1, 2, 3, 4, 5, 6, 7, 8, 9]
	sumsr = []
	sumsc = []
	squares = []
	sumsr += [item for item in sudoku]
	sumsc += [item for item in zip(*sudoku)]
	#print (square(sudoku))
	for x,i in enumerate(sudoku):
		for y,j in enumerate(zip(*sudoku)):
				if ( x // 3 == 0 and y // 3 == 0 and x == y):
					print(i,j)
	#return res == sumsr and res == sumsc

#def square(matrix):

def main():
	print(sudoku_solved([
			[4, 5, 2, 3, 8, 9, 7, 1, 6],
			[3, 8, 7, 4, 6, 1, 2, 9, 5],
			[6, 1, 9, 2, 5, 7, 3, 4 ,8],
			[9, 3, 5, 1, 2, 6, 8, 7, 4],
			[7, 6, 4, 9, 3, 8, 5, 2, 1],
			[1, 2, 8, 5, 7, 4, 6, 3, 9],
			[5, 7, 1, 8, 9, 2, 4, 6, 3],
			[8, 9, 6, 7, 4, 3, 1, 5 ,2],
			[2, 4, 3, 6, 1, 5, 9, 8, 7]
			]))
	# print(sudoku_solved([
	# 		[1, 2, 3, 4, 5, 6, 7, 8, 9],
	# 		[1, 2, 3, 4, 5, 6, 7, 8, 9],
	# 		[1, 2, 3, 4, 5, 6, 7, 8, 9],
	# 		[1, 2, 3, 4, 5, 6, 7, 8, 9],
	# 		[1, 2, 3, 4, 5, 6, 7, 8, 9],
	# 		[1, 2, 3, 4, 5, 6, 7, 8, 9],
	# 		[1, 2, 3, 4, 5, 6, 7, 8, 9],
	# 		[1, 2, 3, 4, 5, 6, 7, 8, 9],
	# 		[1, 2, 3, 4, 5, 6, 7, 8, 9]
	# 		]))
if __name__ == '__main__':
	main()