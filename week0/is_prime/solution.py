def is_prime(n):
	n = abs(n)
	return sum_of_divisors(n) == n + 1

def sum_of_divisors(n):
	result = 0
	divisor = n

	while divisor != 0:
		if n % divisor == 0:
			result = result + divisor
		divisor = divisor - 1

	return result

if __name__ == '__main__':
	main()
