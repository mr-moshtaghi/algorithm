def search_range(nums: list, target: int) -> list:
    low, high = 0, len(nums) - 1

    while low <= high:
        mid = (low + high) // 2
        if target > nums[mid]:
            low = mid + 1
        elif target < nums[mid]:
            high = mid - 1
        else:
            break

    start = mid
    end = mid

    while True:
        if nums[start-1] == target:
            start -= 1
        if nums[end+1] == target:
            end += 1

        if nums[start - 1] and nums[end + 1] != target:
            break
    return [start, end]


print(search_range([1, 2, 2, 2, 3, 3, 3, 4, 4, 5, 5, 5, 5, 7, 7, 7, 9, 9, ], 4))
