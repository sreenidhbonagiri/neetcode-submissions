class Solution:
    # Okay so I remember to use the monotonic stack approach. We can create our stack and result list. Stack will store the indexes, and result will store the number of days or the subtraction of indexes. And so we can loop through the temperatures list by enumerating it so we can also have access to the index. And so we can first check if the index element at the top of the stack is greater than our current temperature, if it is then we can pop that element from the stack but store that index, and then add that to our result list
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        result = [0] * len(temperatures)

        for index, temperature in enumerate(temperatures):
            while stack and temperature > temperatures[stack[-1]]:
                popped_index = stack.pop()
                days = index - popped_index
                result[popped_index] = days
            
            stack.append(index)

        return result



        