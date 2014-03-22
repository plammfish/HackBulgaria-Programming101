def sum_of_divisors(n):
	result = 0
	divisor = n

	while divisor != 0:
		if n % divisor == 0:
			result = result + divisor
		divisor = divisor - 1

	return result

def main():
	print(sum_of_divisors(8))
	print(sum_of_divisors(7))
	print(sum_of_divisors(1))
	print(sum_of_divisors(1000))

if __name__ == '__main__':
	main()