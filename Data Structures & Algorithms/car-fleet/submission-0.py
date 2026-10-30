class Solution:
    # So I would calculate the arrival times of each car, and figure that out. Then if a car has less than or equal to arrival time as another car, that would count as a fleet. But if the car has a greater arrival time than a car ahead of it, it will form its seperate fleet. Very simple process. 
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        cars = sorted(zip(position, speed), reverse = True)
        fleets = 0
        last_fleet_time = 0

        for position, speed in cars:
            time = (target - position) / speed
            
            if time > last_fleet_time:
                fleets += 1
                last_fleet_time = time

        return fleets
              





        

        


        