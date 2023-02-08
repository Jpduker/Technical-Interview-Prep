def twoSum(self, numbers: List[int], target: int):
    res=[]
    
    #Array = [2,5,6,7,9] , target =9 
    left, right =0, len(numbers) -1
    while left< right:
        twoSum= numbers[left]+numbers[right]
        if twoSum < target:
            left +=1
        elif twoSum > target:
            right-=1
        if twoSum == target:
            return [left+1 ,right+1]