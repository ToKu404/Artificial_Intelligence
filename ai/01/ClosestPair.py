import math

def euclid_distance(p1, p2):
  return math.sqrt((p1.x - p2.x)**2 + (p1.y - p2.y)**2)

def brute_force_closest(P):
    min_d = float('inf')
    for i in range(len(P)):
        for j in range(i + 1, len(P)):
            if euclid_distance(P[i], P[j]) < min_d:
                min_d = euclid_distance(P[i], P[j])
    
    return min_d

class Point():
    def __init__(self, x, y):
        self.x = x
        self.y = y

input = [Point(5,2), Point(2,7), Point(10,16),
          Point(34,50), Point(3,6), Point(20,5),
          Point(12,4), Point(8,9), Point(5,21)]
          
cp = brute_force_closest(input)
print("Closest Pair :", cp)
