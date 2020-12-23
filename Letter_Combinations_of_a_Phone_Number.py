class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        a=['_','1','abc','def','ghi','jkl','mno','pqrs','tuv','wxyz']
        def f(string,n):
            if(n==1):
                return(list(a[int(string[n-1])]))
            elif(n==0):
                return([])
            else:
                concerned=list(a[int(string[n-1])])
                remaining=f(string,n-1)
                arr=list()
                for i in concerned:
                    for j in remaining:
                        arr.append(j+i)
                return(arr)
        return(f(digits,len(digits)))
