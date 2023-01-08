def plusOne(self, digits):
        
    length =len(digits) 
    num=0
    res=[]
    
    #[1,2,3] i=1 10^2 , i=2*10^1 , i =3*10^0
    for i in digits:
        num =num + i*pow(10,length-1) 
        length-=1  # 2 , 1, 0
    num+=1
    num=str(num)
    res =[int(x) for x in num]
    return res
        
