class Solution:
    # Write code below to complete prompt
    def isPalindrome(self, s):
            #type s: string
            #return type: boolean
            if (len(s) <= 6):
                 return False
            g = s[::-1]
            if (g == s):
                return True
            return False
            
            
            #TODO: Write code below to return a boolean value with the solution to the prompt.
            pass

def main():
    tc1 = Solution()
    inpyt = input()
    # Write code below to complete prompt
    print(tc1.isPalindrome(inpyt))

if __name__ == "__main__":
    main()
