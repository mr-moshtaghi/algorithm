"""

    [1, 2, 3, 4, 5]
        min 3 => [3, 4, 5]
        max 3 => [1, 2, 3]
        min , max 3 => [3]

        complexity = O(n)

"""


def limit(arr, min=None, max=None):
    min_checked = lambda value: True if min is None else (value >= min)
    max_checked = lambda value: True if max is None else (value <= max)

    return [val for val in arr if min_checked(val) and max_checked(val)]


def limit1(arr, min_lim=None, max_lim=None):
    if len(arr) == 0:
        return arr

    if min_lim is None:
        min_lim = min(arr)
    if max_lim is None:
        max_lim = max(arr)

    return list(filter(lambda x: (min_lim <= x <= max_lim), arr))


print(limit([5, 9, 1, 3, 12, 8, 2, 7, 20, 6], 5, 10))
print(limit1([5, 9, 1, 3, 12, 8, 2, 7, 20, 6], 5, 10))
