import heapq

def kClosest(points,k):
        minHeap = []
        for x,y in points:
            dist = (x**2)+(y**2)
            minHeap.append([dist,x,y])
        heapq.heapify(minHeap)
        res = []
        while k:
            dist, x, y =heapq.heappop(minHeap)
            res.append([x,y])
            k-=1
        return res
points =[[1,3],[2,-2],[-3,3]]

print(kClosest(points,2))