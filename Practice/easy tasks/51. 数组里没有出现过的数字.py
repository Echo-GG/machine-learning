# 给定一个长度为n的正整数数组nums，其中nums[i]的值都在区间[1,n]中，
# 请找出nums数组在[1,n]范围里面没有出现过的数字，并将他们放在数组里面返回（在数组里面的顺序可以不唯一）
def func(nums):
    l = [i for i in range(1,len(nums)+1)]
    l2 = []
    # nums = set(nums) # e.g. nums = [1,2,3,2,1] --> nums = [1,2,3]
    for i in l:
        if i in nums:
            continue
        else:
            l2.append(i)

    return l2

l = [2,3,1,2,3,4,1]
print(func(l))
