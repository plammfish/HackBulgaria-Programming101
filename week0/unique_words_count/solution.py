def unique_words_count(arr):
    result = {}
    for item in arr:
        if item in result:
            result[item] += 1
        else:
            result[item] = 1

    return len(result)

