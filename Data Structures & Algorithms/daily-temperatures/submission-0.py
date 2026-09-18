class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        
        temp_stack = []
        res = [0] * len(temperatures)
        current_temp = float("-inf")
        edited_temps = []

        for i in range(len(temperatures)):
            if current_temp < temperatures[i]:

                for index, item in enumerate(temp_stack):
                    if item[1] < temperatures[i]:
                        res[item[0]] = i - item[0]
                        edited_temps.append(item)

                for item in edited_temps:
                    temp_stack.remove(item)

                edited_temps.clear()

            temp_stack.append((i, temperatures[i]))
            current_temp = temperatures[i]


        return res