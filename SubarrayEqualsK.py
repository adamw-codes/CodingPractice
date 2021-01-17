class Solution:
    def subarraySum(self, nums, k):
        # key is for the sum and value is the number of occurences
        map = {0:1}
        runningSum = 0
        arrayLength = len(nums)
        count = 0
        # for loop go through the array
        for i in range(arrayLength):
            runningSum = nums[i] + runningSum
            # this is to check if you have enough remaining to reach that sum of k
            if runningSum-k in map:
                # then you increment count by the number of counts there are at that key
                count = map[runningSum-k] + count
            # this is to update the map in the case that the key has already been inputted so there are no duplicated
            if runningSum in map:
                map[runningSum] = map[runningSum] + 1
            # this is if there are no entries for that key
            else:
                map[runningSum] = 1
        return count

test = Solution()
print(test.subarraySum([3,4,7,2,-3,1,4,2], 7))