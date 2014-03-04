def sum_of_digits(n):

	result = 0
	n = abs(n)

	while n != 0:
		result = result +  n % 10
		n = n // 10

	return result

def main():
	print (sum_of_digits(-71))
	print(sum_of_digits(81))

if __name__ == '__main__':
	main()

