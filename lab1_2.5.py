def merge_intervals(intervals):
    
    intervals.sort(key=lambda x: x[0])
    
    merged_intervals = []
    
    for interval in intervals:
        if not merged_intervals or interval[0] > merged_intervals[-1][1]:

            merged_intervals.append(interval)
        else:
            merged_intervals[-1] = (merged_intervals[-1][0], max(merged_intervals[-1][1], interval[1]))
    
    return merged_intervals

intervals = [(1, 4), (2, 5), (7, 8), (6, 9)]
non_overlapping_intervals = merge_intervals(intervals)
print("Non-overlapping intervals after merging:", non_overlapping_intervals)
