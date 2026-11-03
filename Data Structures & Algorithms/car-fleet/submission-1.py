class Solution:
    # Okay so for this problem, we can first check when each car will reach the target individually. Then we can sort them from closest to farthest and zip them into a tuple so each element can have be sorted by position. Then we can check 
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        cars = sorted(zip(position, speed), reverse = True)

        fleet = 0
        fleet_time = 0 

        for position, speed in cars:
            time = (target - position) / speed

            if time > fleet_time:
                fleet += 1
                fleet_time = time

        return fleet
    

            




         

            


        


        