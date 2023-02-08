def maxArea(self, height: List[int]) -> int:
    maxArea = 0
    left , right = 0,len(height)-1
    
    while left<right:
        width = right - left 
        maxArea = max(maxArea , min(height[left], height[right])*width)
        if height[left] >height[right]:
            right -=1
        else :
            left +=1
    return maxArea