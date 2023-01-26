def climbStairs(self, n: int) -> int:
    if n==1:
        return 1
    #base condition
    first=1
    second=2
    
    for i in range(3,n+1):
        
        # 1 2 3 5 8 13
        #       ^ ^ ^
        
        third=first + second
        
        first = second
        second = third
        
    return second