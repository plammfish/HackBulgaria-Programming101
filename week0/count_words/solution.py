def count_words(arr):
    result = {}
    for item in arr:
        if item in result:
            result[item] += 1
        else:
            result[item] = 1

    return result
