def more_than_three(products):
    count = 0
    result = []
    for i in range(len(products)):
        for j in range(i):
            if products[j] > 3:
                count += 1
        result.append(count)
        count = 0
    return result
