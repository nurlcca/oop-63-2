def find_element(array, target):
    for i in array:
        if i == target:
            print("+")
    else:
        print("-")

def binary_search(array, target):
    left, right = 0, len(array) - 1
    while left <= right:
        mid = (left + right) // 2
        if array[mid] == target:
            print("+")
            break
        elif array[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    else:
        print("-")

nums = [2, 7, 11, 15]
target = 9

def two_sum(nums, target):
    num_map = {}
    for i, num in enumerate(nums):
        complement = target - num
        if complement in num_map:
            return [num_map[complement], i]
        num_map[num] = i
    return []

two_sum(nums, target)
print(two_sum(nums, target))
