class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        x1,y1 = 0,0
        hashmap = {}
        for x,y in points:
            point=(x,y)
            dist = sqrt((x-x1)**2 + (y-y1)**2)
            hashmap[point] = dist
            print(dist)
        for i in range
        print(hashmap)

