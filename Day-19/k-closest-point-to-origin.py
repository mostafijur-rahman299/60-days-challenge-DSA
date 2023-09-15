import math

points = [[1,3],[-2,2]]

k = 1

euclidean_point = []

for point in points:
    euclidean_point.append(math.sqrt(abs(point[0] ** 2 + point[1] ** 2)))
    
euclidean_point = sorted(enumerate(euclidean_point), key=lambda x: x[1])

result = []

for i, point in euclidean_point[:k]:
    result.append(points[i])

print(result)