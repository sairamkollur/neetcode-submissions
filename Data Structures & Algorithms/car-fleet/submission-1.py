class Solution:
    def carFleet(self, target: int, position: list[int], speed: list[int]) -> int:

        cars = {}

        for p, s in zip(position, speed):
            cars[p] = s

        stack = []

        for p in sorted(cars.keys(), reverse=True):
            time = (target - p) / cars[p]

            if not stack or time > stack[-1]:
                stack.append(time)

        return len(stack)