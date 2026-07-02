class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = [0] * len(temperatures)
        
        # The stack will store pairs of [temperature, index]
        # It maintains temperatures in decreasing order (a monotonic decreasing stack)
        stack = [] 
        
        for i, t in enumerate(temperatures):
            # While the stack is not empty AND the current temperature (t) 
            # is greater than the temperature at the top of the stack:
            while stack and t > stack[-1][0]: 
                
                # Pop the colder temperature from the stack
                stackTemp, stackInd = stack.pop()
                
                # Calculate the number of days waited and store it in the result array
                res[stackInd] = i - stackInd
                
            # Push the current temperature and its index onto the stack to wait for a warmer day
            stack.append([t, i])
            
        return res