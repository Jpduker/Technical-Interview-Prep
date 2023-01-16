""" Step 1: Fix Two pointers left and right which will point to begining and endo of the strings 
    Step 2: While left<right and element at the left and right indeces are not aplhanumerics(a-z or 0-9) just increment the pointer
    Step 3: If the element at the left and right indeces are not equal we return False
    Step 4: If the element at left and right indeces are equal we just increment left and decrement right
    Step 5: If left<right condition is not true it means we traversed all the elements and all are equal and
            hence it is a valid palindorme. 

"""


def isPalindrome(s):
    left,right = 0,len(s)-1

    while(left<right):
        while(left<right) and not s[left].isalnum():
            left+=1
        while(left<right) and not s[right].isalnum():
            right-=1
        if left<right and s[left].lower() !=s[right].lower():
            return False
        
        left+=1
        right-=1
        
    return True

print(isPalindrome("race a car"))