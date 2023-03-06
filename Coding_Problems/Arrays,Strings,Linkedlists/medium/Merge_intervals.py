def merge( intervals) :
        intervals.sort(key =lambda i:i[0])
        output = [intervals[0]]

        for start ,end in intervals[1:]:
            lastend = output[-1][1]

            if start <= lastend:
                output[-1][1] = max(lastend,end)
            else:
                output.append([start,end])
        return output
intervals =[[1,3],[2,5] ,[6,8] ,[9,11]]

print(merge(intervals))