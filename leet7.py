class Solution:
    def reverse(self, x: int) -> int:
        if(x>=0):
            x=str(x)
            x=x[::-1]
            x=int(x)
            if x >= 2**31:
                return 0
            return x
        elif(x<0):
            x=0-(x)
            x=str(x)
            x=x[::-1]
            x=int(x)
            x=0-x
            if x <= -2**31:
                return 0
            return x
        