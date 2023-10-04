intervals = [[1,4],[0,0]]
intervals = sorted(intervals, key=lambda x: x[0])
ans = []

for interval in intervals:
    if not ans or ans[-1][1] < interval[0]:
        ans.append(interval)
    else:
        ans[-1][1] = interval[1]
        
print(ans)
