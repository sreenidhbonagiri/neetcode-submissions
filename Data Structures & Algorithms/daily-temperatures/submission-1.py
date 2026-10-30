class Solution:
    # So we can first create a stack list, and a result list where every element is 0 to begin with. Then we can loop through each temperature in our temperatures list whilst keeping track of their indexes so use enumerate. Then we can check to see if the current temperature is greater than the temperature already in our stack, and if it is then we can immediately pop it and keep track of the index. Then calculate that wait time. Then push that wait time value into its corresponding index in the result list.
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        result = [0] * len(temperatures)

        for index, temp in enumerate(temperatures):
            while stack and temp > temperatures[stack[-1]]:
                prev_index = stack.pop()
                wait_time = index - prev_index
                result[prev_index] = wait_time
            
            stack.append(index)

        return result
            







