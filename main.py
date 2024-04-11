from typing import List

def twoSum(nums: List[int], target: int) -> List[int]:
    tmp = {}
    n = len(nums)

    for i in range(n):
        comp = target - nums[i]

        if comp in tmp and tmp[comp] != i:
            return [tmp[comp], i]
        else:
            tmp[nums[i]] = i

    return
