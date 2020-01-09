class Solution:
    def __init__(self):
        self.res = list()
        print("784lletcode")

    def solve(self,instr,i):
        n = len(instr)
        print("solve",instr,"i",i,"n",n)
        if n==i:
            self.res.append(instr)
            return 
        self.solve(instr,i+1)
        if ord(instr[i])>=65:
            a=chr(ord(instr[i])^(1<<5))
            instr = instr[:i]+a+instr[i+1:]
            print("new",instr)
            self.solve(instr,i+1)


        

if __name__ == "__main__":
    s = Solution()
    a = "13r5b"
    #s.solve(a,0)
    s.solve2(s)
    for i in s.res:
        print(str(i,'utf-8'))
