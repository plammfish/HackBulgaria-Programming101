def is_an_bn(word):
    n = len(word)
    n2 = len(word) // 2
    if n % 2 != 0:
        return False
    else:
        return word == ("".join("a" * n2)) + ("".join("b" * n2))
