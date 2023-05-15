"""

    [1, 2, 1, 3, 4, 2] => [1, 2]

    complexity = O(n)

"""


def top_one(arr):
    value = {}
    result = []

    for i in arr:
        if i in value:
            value[i] += 1
        else:
            value[i] = 1

    max_arr = max(value.values())

    for i in value:
        if value[i] == max_arr:
            result.append(i)

    return result, max_arr


print(top_one([1, 2, 1, 3, 4, 2]))
