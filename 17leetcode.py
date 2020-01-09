class Test:
    def __init__(self):
        self.map = {"":"","1":"abc","2":"def","3":"ghi","4":"jkl","5":"mno"} 
        self.res = [""]
        print("this is Test init")    
    
    def letterCombine(self,digits):
        for index,value in enumerate(digits):
            letter = self.map[value]
            print("type arr:",letter)
            while index==len(self.res[0]):
                pop = self.res.pop(0)
                print("pop:",pop)
                for j in list(letter):
                    temp=pop+j
                    print(temp,j)
                    self.res.append(temp)
                                        

    def display(self):
        for i in self.res:
            print("result:",i)
        
               
t = Test()
t.letterCombine("23")
t.display()
