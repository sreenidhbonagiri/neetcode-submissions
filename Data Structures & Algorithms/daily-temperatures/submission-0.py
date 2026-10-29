class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        answer = [0] * len(temperatures)


        for index, temperature in enumerate(temperatures):
            while stack and temperature > temperatures[stack[-1]]:
                prev_index = stack.pop()
                wait = index - prev_index
                answer[prev_index] = wait
            else:
                stack.append(index)

        return answer



