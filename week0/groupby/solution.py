def groupby(func, seq):
    result = {}
    for item in seq:
        if func(item) in result:
            result[func(item)] = result[func(item)] + [item]
        else:
            result[func(item)] = [item]

    return result
