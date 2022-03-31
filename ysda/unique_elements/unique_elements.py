def uniq(elements):
    dict = {}
    for elem in elements:
        if elem in dict:
            dict[elem] += 1
        else:
            dict[elem] = 1

    return [elem for elem, count in dict.items() if count == 1]
