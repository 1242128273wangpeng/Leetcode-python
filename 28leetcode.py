class strStr:
    def __init__(self):
        print("strStr init")

    def implement(self,haystack,needle):
        h = len(haystack)
        n = len(needle)

        for i in range(0,h-n+1):
            print("i:",i)
            for j in range(0,n):
                print("j:",j)
                if haystack[i+j]!=needle[j]:
                    print("no equal:",j)
                    break
                else:
                    print("equal:","j:",j,"n:",n)
                    if j+1==n:
                        return i;
           
        return -1

ss = strStr()
#print ss.implement("mississippi","issip")
print(ss.implement("",""))
