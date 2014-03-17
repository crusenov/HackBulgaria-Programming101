def sevens_in_a_row( arr, n ):
  count = 1
  for i in range(0, len(arr) - 1):
      if arr[i] == 7:
        if arr[i] == arr[i+1]:
            count += 1
  if count >= n:
    return True
  else:
    return False

def main():
	print(sevens_in_a_row([7,7,7,1,1,1,7,7,7,7],3))

if __name__ == '__main__':
	main()
    