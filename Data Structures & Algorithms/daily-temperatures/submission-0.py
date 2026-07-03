class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
      n= len(temperatures)
      result = [0] * n
      stack = []
      for i , temp in enumerate(temperatures):
        while stack and temp > temperatures[stack[-1]]:
            prev_i = stack.pop()
            result[prev_i] = i - prev_i
        stack.append(i)
      return result