"""

complexity = O(log n)

"""

def search_insert(arr, value):
    low = 0
    high = len(arr) - 1
    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == value:
            return mid
        elif value > arr[mid]:
            low = mid + 1
        else:
            high = mid - 1
    return low


print(search_insert([1, 3, 4, 6], 5))
