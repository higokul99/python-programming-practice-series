class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        pattern_count = len(pattern)
        s_list = s.split(" ")
        s_list_count = len(s_list)
        print(pattern_count)
        print(s_list)
        print(s_list_count)
        if pattern_count == s_list_count:
            return False

        
        
            
        



# pattern = input("Enter Pattern :")
# s = input("Enter the s:")

pattern = "aba"
s = "apple ball apple"

c = Solution()
result = c.wordPattern(pattern,s)
print(result)
