def max_activities(activities):
    activities.sort(key=lambda x: x[1])

    selected_activities = []
    prev_finish_time = float('-inf')
    
    for activity in activities:
        start, finish = activity
        
        if start >= prev_finish_time:
            selected_activities.append(activity)
            prev_finish_time = finish
    
    return selected_activities

activities = [(1, 4), (3, 5), (0, 6), (5, 7), (3, 8), (5, 9), (6, 10), (8, 11), (8, 12), (2, 13), (12, 14)]
selected_activities = max_activities(activities)
print("Maximum number of activities performed by a single person:", selected_activities)
