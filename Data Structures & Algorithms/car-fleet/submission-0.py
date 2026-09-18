class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        times = []
        arrival_list = []
        for car in range(len(position)):
            arrival = (target - position[car]) / speed[car]
            times.append((position[car], arrival))

        times.sort(key=lambda x: x[0], reverse=True)

        for car, arrival_time in times:
            if not arrival_list:
                arrival_list.append(arrival_time)
            else:
                if arrival_time > arrival_list[-1]:
                    arrival_list.append(arrival_time)

        return len(arrival_list)


        