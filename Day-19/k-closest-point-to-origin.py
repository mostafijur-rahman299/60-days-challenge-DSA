import math

points = [[3,3],[5,-1],[-2,4]]

k = 2

euclidean_point = []

for point in points:
    euclidean_point.append(math.sqrt(abs(point[0] ** 2 + point[1] ** 2)))
    
euclidean_points = sorted(euclidean_point)


result = []

for item in euclidean_points[:k]:
    value_index = euclidean_point.index(item)
    result.append(points[value_index])
    
print(result)
