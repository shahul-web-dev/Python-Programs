class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        numIndices = {}
        for index, value in enumerate(nums):
            neededNum = target - nums[index]

            if neededNum in numIndices:
                return [index, numIndices[neededNum]]

            numIndices[value] = index
