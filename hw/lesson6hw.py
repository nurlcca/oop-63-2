nums = [2, 7, 11, 15]
target = 9

def two_sum(nums, target):
    for i in range(len(nums)):              # first loop
        for j in range(i + 1, len(nums)):   # second loop
            if nums[i] + nums[j] == target:
                return [i, j]

print(two_sum(nums, target))