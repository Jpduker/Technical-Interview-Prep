def decodeString(self, s: str) -> str:
        stack =[]
        for i in range(len(s)):
            
            #we add all the elements of the string into a stack except the closing bracket
            if s[i] != "]":
                stack.append(s[i])
                
            #when we encounter a closing bracket, we pop all the elements from the stack until we encounter an opening bracket
            else:
                substr=""
                while stack[-1] != "[": 
                    substr = stack.pop() +substr
                stack.pop()#we pop the opening bracket also
                k=""
                #once the opening bracket is popped, we pop all the digits from the stack and add them to k
                while stack and stack[-1].isdigit():
                    k = stack.pop() + k
                #after we have the number and the string, we add the string to the stack the number of times the number says
                stack.append(int(k)* substr)
        #atlast we return the stack as a string
        return "".join(stack)