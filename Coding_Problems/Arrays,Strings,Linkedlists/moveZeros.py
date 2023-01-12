def moveZeroes(nums):
    res = []
    res2 =[]
    for i in range(len(nums)):
        if nums[i]==0:
            res2.append(nums[i])
        else:
            res.append(nums[i])

    for i in res2:
        res.append(i)

    return res

print(moveZeroes(([1,6,0,3,7,0])))
        