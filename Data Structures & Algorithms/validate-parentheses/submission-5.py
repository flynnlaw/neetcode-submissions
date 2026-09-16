class Solution:

    def tryRemove(self, stack:List[str], s):
        end = len(stack)-1
        try:
            if stack[end] == s: 
                stack.pop()
            else: 
                return False
        except:
            return False

    def isValid(self, s: str) -> bool:

        if len(s) == 1: 
            return False
        
        res=True

        stack = []
        for i in s:
            if i == '(':
                stack.append('(')
            elif i == '[':
                stack.append('[')
            elif i == '{':
                stack.append('{')
            elif i == ')':
                res=self.tryRemove(stack, '(')
            elif i == ']':
                res=self.tryRemove(stack, '[')
            elif i == '}':
                res=self.tryRemove(stack, '{')

            if res == False:
                return False
        
        if stack:
            return False
        else: 
            return True
            
    
    
                

