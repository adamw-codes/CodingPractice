class Solution:
    def lengthOfLongestSubstring(self, s: str):
        # calculate length of string
        stringLength = len(s)
        # determine is an empty string is given
        if stringLength == 0:
            return 0
        # using dictionary to map out the string, keys are the characters and the values are the index positions
        # this is because we have access to characters and will use those to determine positions
        characters = {}
        max_length = 0
        start = 0
        # for loop to iterate through the string
        for i in range(stringLength):
            # this is used to determine whether the character is already in the string (repeated character means end of substring)
            # and we need to make sure that the start position is behind the position we are at so we can update the start for the new substring that is about to start
            # just because the character is in characters does not mean that is repeated (substring ends so new substring starts) so that is also why we have the second condition
            if s[i] in characters and start <= characters[s[i]]:
                # move start to one position before current position for new substring
                start = characters[s[i]] + 1
            # if a repeated character is not detected 
            else:
                # have the max length calculated as we are running
                max_length = max(max_length, i - start + 1)
            # put the value into the dictionary
            characters[s[i]] = i

        return max_length

test = Solution()
print(test.lengthOfLongestSubstring("aaaaaaaaa"))