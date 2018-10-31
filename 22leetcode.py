class GenerateParenthsis:
    def __init__(self):
        self.res = []
        print "GenerateParenthsis"
    
    def generate(self,length):
        half = length/2
        self.create(half,half,"")

    def create(self,leftrem,rightrem,buff):
        print "buff:",buff
        if leftrem<0 or rightrem<leftrem:
            return
        if rightrem==0 and leftrem==0:
            self.res.append(buff)
            print "buff add:",buff
            return
        else:
            if leftrem>0:
                self.create(leftrem-1,rightrem,buff+"{")
            if leftrem<rightrem:
                self.create(leftrem,rightrem-1,buff+"}")
    
    def display(self):
        for i in self.res:
            print "display:",i

gp = GenerateParenthsis()
gp.generate(4)
gp.display()



    
