def nth_fibonacci(n):
    a = 0
    b = 1
    index = 1

    while index != n:
        next = a + b
        a = b
        b = next
        index = index + 1

    return b
