class Solution:
    def countBits(self, n: int) -> List[int]:
        output = []

        for i in range(n+1):
            a = bin(i).count('1')
            output.append(a)
        
        return output