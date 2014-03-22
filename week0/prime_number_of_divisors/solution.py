def prime_number_of_divisors(n):
	result = number_of_divisors(n)
	return is_prime(result)

def number_of_divisors(n):
	result = 0
	divisor = n

	while divisor != 0:
		if n % divisor == 0:
			result = result + 1
		divisor = divisor - 1

	return result

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
