# B.F

values = [1, 2, 34, 5, 6, 7, 8, 8, 10]

target = 9


def two_sum_BF(nums):
    for i, num in enumerate(nums):
        remaing = target - num
        for x in range(i + 1, len(nums)):
            if nums[x] == remaing:
                flag = True
                return (i, x)
        return ()


print(two_sum_BF(values))
