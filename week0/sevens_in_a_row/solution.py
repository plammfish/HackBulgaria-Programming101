def sevens_in_a_row(arr, n):
	result = 0
	biglamp = False

	for item in arr:
		if item == 7:
			result = result + 1
		if item != 7:
			lamp = result == n
			if lamp:
				biglamp = True
			result = 0

	return biglamp

if __name__ == '__main__':
	main()

