class Solution:
    # [ (7,1), (4,2), (1,2), (0,1) ]
    # first pass - fleet_time = 3 and fleet = 1
    # second pass - fleet_time = 3 and fleet = 1
    # third pass - fleet_time = 4 and fleet = 2
    # fourth pass - fleet_time = 10 and fleet = 3
    # return 3
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



