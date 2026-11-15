class Solution:
    def carFleet(self, target: int, positions: list[int], speeds: list[int]) -> int:
        cars = sorted(
            list(zip(positions, speeds)), key=lambda car: car[0], reverse=True
        )
        fleet: list[float] = []
        for car in cars:
            position, speed = car
            arrivalTime = (target - position) / speed
            if len(fleet) <= 0:
                fleet.append(arrivalTime)
                continue
            previousFleetArrivalTime = fleet.pop()
            if previousFleetArrivalTime >= arrivalTime:
                fleet.append(previousFleetArrivalTime)
                continue
            fleet.append(previousFleetArrivalTime)
            fleet.append(arrivalTime)
        return len(fleet)


if __name__ == "__main__":
    solution = Solution()
    result = solution.carFleet(12, [10, 8, 0, 5, 3], [2, 4, 1, 1, 3])
    print(result)  # should print out 3
