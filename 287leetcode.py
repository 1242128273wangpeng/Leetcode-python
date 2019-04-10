class Solution:
    def __init__(self):
        print "leetcode 287"

    def findDuplicate(self,nums):
        if len(nums)>1:
            slow = nums[0]
            fast = nums[nums[0]]
            while slow != fast:
                slow = nums[slow]
                fast = nums[nums[fast]]
                print slow,fast
            print "find slow:",slow,"fast:",fast
            entry = 0
            while entry != slow:
                entry = nums[entry]
                slow = nums[slow]
                print "res slow:",slow,"entry",entry
            return entry
        return -1
    

if __name__ == "__main__":
    s = Solution()
    a = [2,2,3,4,5,6,7,3]
    s.findDuplicate(a)

