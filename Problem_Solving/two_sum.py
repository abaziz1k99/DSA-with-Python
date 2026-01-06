# B.F

values = [1, 2, 34, 5, 6, 7, 8, 8, 10]

target = 9


def two_sum_BF(nums):
    for i, num in enumerate(nums):
        remaining = target - num
        for x in range(i + 1, len(nums)):
            if nums[x] == remaining:
                flag = True
                return (i, x)
    return ()


def two_sum_hash(nums: list) -> tuple:
    seen = {}

    for i, num in enumerate(nums):
        remaining = target - num
        if remaining in seen:
            return (seen[remaining], i)
        seen[num] = i


print(two_sum_hash(values))
print(two_sum_BF(values))
