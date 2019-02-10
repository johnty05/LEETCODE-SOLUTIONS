class Solution:
    def letterCombinations(self, digits):
        self.m = ['','','abc','def','ghi','jkl','mno','pqrs','tuv','wxyz']
        self.res = []
        self.addLetter(digits, 0, "")
        return self.res

    def addLetter(self,digits, curr,path):
        if curr == len(digits):
            if path:
                self.res.append(path)
            return
        
        for j in self.m[int(digits[curr])]:
            self.addLetter(digits, curr+1, path+j)
