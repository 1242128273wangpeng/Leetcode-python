def canPartition(nums):
    half_sum = sum(nums)
    if half_sum%2 == 1:
        return False
    half_sum = half_sum/2
    d = [[False for x in xrange(half_sum + 1)] for y in xrange(len(nums)+1)]
    print d
    for k in xrange(len(nums)+1):
        d[k][0] = True
    for i in xrange(1,len(nums)+1):
        for j in xrange(0,half_sum+1):
            d[i][j] = d[i-1][j]
            if j>= nums[i-1]:
                d[i][j] = d[i][j]|d[i-1][j-nums[i-1]]
    print d
    return d[len(nums)][half_sum]


def canPartition2(nums):
    total = sum(nums)
    if total&1:
        return 
    d = [0 for j in range(total+1)] 
    print d
    d[0] = 1
    print d 
    for v in nums:
        for i in range(total,-1,-1):
            if d[i]:
                d[i+v] = 1
        if d[total/2]:
            return True
    return False

        

if __name__ == "__main__":
    a = [3,5,4,2,6,4]
    print "1:",canPartition(a)
    print "2:",canPartition2(a)
