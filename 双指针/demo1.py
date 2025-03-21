class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        dest = 0
        for cur in range(len(nums)):
            if nums[cur]:
                nums[cur], nums[dest] = nums[dest], nums[cur]
                dest += 1
