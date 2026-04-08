class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        lst = []
        for i in range(len(speed)):
            time = (target-position[i])/speed[i]
            lst.append([position[i],time])
        lst.sort(reverse=True)
        print(lst)
        fleet = 0
        maxtime = 0
        # car.append(lst.pop())
        for pos,time in lst:
            if time > maxtime:
                fleet += 1
                maxtime = time
            # car.append([pos,time])
        return fleet