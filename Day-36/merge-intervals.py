intervals = [[1,4],[0,0]]
non_intervals = []

non_intervals.append(intervals[0])

for index in range(1, len(intervals)):
    non_interval_last_item = non_intervals[len(non_intervals)-1]
    if non_interval_last_item[1] >= intervals[index][0]:
        if non_interval_last_item[1] < intervals[index][1]:
            non_intervals[len(non_intervals)-1][1] = intervals[index][1]
        
        if non_interval_last_item[0] > intervals[index][0]:
            non_intervals[len(non_intervals)-1][0] = intervals[index][0]
    else:
        non_intervals.append(intervals[index])

print(non_intervals)