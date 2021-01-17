class Solution:
    def threeSum(self, nums):
        result = []
        nums.sort()
        arrLength = len(nums)
        for i in range(arrLength-2):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            left = i + 1
            right = arrLength - 1
            while left < right:
                tempSum = nums[i] + nums[left] + nums[right]
                if tempSum < 0:
                    left = left + 1
                if tempSum > 0:
                    right = right - 1
                if tempSum == 0:
                    result.append([nums[i], nums[left], nums[right]])
                    while left < right and nums[left] == nums[left+1]:
                        left = left + 1
                    while left < right and nums[right] == nums[right-1]:
                        right = right - 1
                    left = left + 1
                    right = right - 1

        return result


test = Solution()
answer = test.threeSum([-1,0,1,2,-1,-4])
print(answer)
                    
