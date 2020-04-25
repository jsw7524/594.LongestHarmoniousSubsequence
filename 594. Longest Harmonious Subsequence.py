class Solution(object):
    def findLHS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        dictNums={}
        for n in nums:
            if n not in dictNums:
                dictNums[n]=1
            else:
                dictNums[n]+=1

        maxLength=0

        for n in nums:
            if n+1 in dictNums:
                if dictNums[n]+dictNums[n+1] > maxLength:
                    maxLength=dictNums[n]+dictNums[n+1]
            if n-1 in dictNums:
                if dictNums[n]+dictNums[n-1] > maxLength:
                    maxLength=dictNums[n]+dictNums[n-1]

        return maxLength

sln=Solution()
assert 5==sln.findLHS([1,3,2,2,5,2,3,7])
assert 5==sln.findLHS([3,2,2,2,3])
assert 8==sln.findLHS([1,3,2,2,5,3,7,2,6,3,9,4,0,23,344,4358,2,3,7])



