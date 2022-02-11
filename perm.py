class permutationstring:
    
    def permutation(self,string):
        if string=='':
            return []
        output=[]

        stack=[]
        index=0
        hashset=set()
        self.backtracking(stack,output,string,index,hashset)
        return output
    def backtracking(self,stack,output,string,index,hashset):
        
        if len(string)==len(stack):
            s=list(stack)
            output.append(''.join(s))
            return
         
        for i in range(0,len(string)):
            if string[i] not in hashset:
                hashset.add(string[i])
                stack.append(string[i])
                
                #print(stack)
                self.backtracking(stack,output,string,i,hashset)
                stack.pop()
                hashset.remove(string[i])
a=permutationstring()
x='abc'
print(a.permutation(x))
    
        
        
            
        
        
    
    