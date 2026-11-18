class Solution:
    def romanToInt(self, s: str) -> int:
        sym_val = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        
        total = 0
        
        for i in range(len(s) - 1):
            if sym_val[s[i]] < sym_val[s[i + 1]]:
                total -= sym_val[s[i]] 
            else:
                total += sym_val[s[i]]  
        total += sym_val[s[-1]]

        return total