class Solution:
    def isHappy(self, n: int) -> bool:

        slow, fast = n, self.sumSquare(n)

        while slow != fast:
            fast = self.sumSquare(fast)
            fast = self.sumSquare(fast)
            slow = self.sumSquare(slow)

        return True if fast == 1 else False
        

    def sumSquare(self, x: int) -> int:
        output = 0

        while x:
            digit = x % 10
            digit = digit ** 2
            output = output + digit
            x= x//10
            
        return output


        