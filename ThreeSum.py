class Solution:
    def threeSum(self, nums):
        # create a list to hold the answers
        result = []
        # sort the list so it easier to determine how to modify the tempSum
        nums.sort()
        arrLength = len(nums)
        # -2 is used in the length to create room for the left and right pointer that would be
        # ahead of the current position
        for i in range(arrLength-2):
            # that i greater than 0 is used to tackle whether all 3 0s are given
            # the second part is to determine there are no duplicates
            if i > 0 and nums[i] == nums[i-1]:
                continue
            # set the pointers to their respective positions
            left = i + 1
            right = arrLength - 1
            # this while loop is used to move the left and right in relation to a particular i
            while left < right:
                # calculate your current sum
                tempSum = nums[i] + nums[left] + nums[right]
                # determine where the sum belongs, and modify the sum value accordingly
                if tempSum < 0:
                    # this are used to skip through any possible duplicates we might get in our answers
                    # duplicates in wrong cases are checked in order to speed up computing time
                    while left < right and nums[left] == nums[left+1]:
                        left = left + 1
                    left = left + 1
                if tempSum > 0:
                    # this are used to skip through any possible duplicates we might get in our answers
                    # duplicates in wrong cases are checked in order to speed up computing time
                    while left < right and nums[right] == nums[right-1]:
                        right = right - 1
                    right = right - 1
                # if sum is found
                if tempSum == 0:
                    # add answer to list
                    result.append([nums[i], nums[left], nums[right]])
                    # these are used to skip through any possible duplicates we might get in our answers
                    while left < right and nums[left] == nums[left+1]:
                        left = left + 1
                    while left < right and nums[right] == nums[right-1]:
                        right = right - 1
                    # move both pointers as a 0 means we need to move both
                    left = left + 1
                    right = right - 1

        return result


test = Solution()
answer = test.threeSum([-1,0,1,2,-1,-4])
print(answer)
                    
