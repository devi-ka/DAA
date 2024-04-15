def maximumPeople(town_population, town_location, cloud_location, cloud_range):
    n = len(town_population)
    m = len(cloud_location)
    
    max_people_sunny = 0

    for i in range(m):
        total_people_sunny = 0

        for j in range(n):
            is_sunny = True
            for k in range(m):
                if abs(town_location[j] - cloud_location[k]) <= cloud_range[k]:
                    is_sunny = False
                    break
            if is_sunny:
                total_people_sunny += town_population[j]

        max_people_sunny = max(max_people_sunny, total_people_sunny)
    
    return max_people_sunny

n = int(input())
town_population = list(map(int, input().split()))
town_location = list(map(int, input().split()))
m = int(input())
cloud_location = list(map(int, input().split()))
cloud_range = list(map(int, input().split()))

print(maximumPeople(town_population, town_location, cloud_location, cloud_range))
