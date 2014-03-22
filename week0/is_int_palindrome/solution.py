def is_int_palindrome(n):
	n = abs(n)
	return n == reverse(n)

def reverse(n):
	result = 0
	n = abs(n)

	while n != 0:
		work = n % 10
		result = result*10 + work
		n = n // 10

	return result

if __name__ == '__main__':
	main()



