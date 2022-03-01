class Solution:
    def countOdds(self, low: int, high: int) -> int:
        d=abs(low-high)
        c=d//2
        
        if high%2==1 or low%2==1:
            c+=1
        return c    