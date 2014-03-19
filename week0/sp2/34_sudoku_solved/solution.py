def get_square(sudoku,i, j):
	return [sudoku[r][c]
			for r in range(0, 9)
			for c in range(0,9)
			if r // 3 == i // 3 and c // 3 == j // 3]

def sudoku_solved(sudoku):
	res = [1, 2, 3, 4, 5, 6, 7, 8, 9]
	rows = []
	cols = []
	squares = [get_square(sudoku, i, j)
				for i in range(0,9)
				for j in range(0,9)]
	rows += [item for item in sudoku]
	cols += [item for item in zip(*sudoku)]
	for row in rows:
		if sorted(row) != res:
			return False
	for col in cols:
		if sorted(col) != res:
			return False
	for square in squares:
		if sorted(square) != res:
			return False
	return True

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
	print(sudoku_solved([
			[1, 2, 3, 4, 5, 6, 7, 8, 9],
			[1, 2, 3, 4, 5, 6, 7, 8, 9],
			[1, 2, 3, 4, 5, 6, 7, 8, 9],
			[1, 2, 3, 4, 5, 6, 7, 8, 9],
			[1, 2, 3, 4, 5, 6, 7, 8, 9],
			[1, 2, 3, 4, 5, 6, 7, 8, 9],
			[1, 2, 3, 4, 5, 6, 7, 8, 9],
			[1, 2, 3, 4, 5, 6, 7, 8, 9],
			[1, 2, 3, 4, 5, 6, 7, 8, 9]
			]))
if __name__ == '__main__':
	main()
