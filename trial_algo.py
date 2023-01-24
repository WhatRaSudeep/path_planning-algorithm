import matplotlib.pyplot as plt
import numpy as np
import shapely as shp
import math

class algo():
    def __init__(self, goal, start):
        self.goal=goal
        self.start=start
        self.path=[start]
        self.step_size=10

    def points(self, node):
        points=[]
        for t in range(0,15):
            unit_vector=[math.sin(t), math.cos(t)]
            points.append([(unit_vector[0]*self.step_size)+float(node[0]),(unit_vector[1]*self.step_size)+float(node[1])])

        return points

    def distance(self, node1, point):
        dist = np.sqrt((node1[0] - point[0]) ** 2 + (node1[1] - point[1]) ** 2)
        return dist

    def closest_point(self, node):
        closest=1000
        tempnode = [200,200]
        for i in (self.points(node)):
            if  (self.distance(i,goal)<closest).all():
                closest = self.distance(i,goal)
                tempnode= i
        self.path.append(tempnode)
        return tempnode

    


goal = [136.93185132643106, 144.37245241440598]
start= [0,0]
rrt = algo(goal,start)
for k in range(0,5):
    print(k)

plt.plot(goal[0],goal[1],'r+')
plt.plot(start[0],start[1],'bo')
goal_notfound=True
while goal_notfound:
    i=rrt.path[len(rrt.path)-1]
    for y in rrt.points(i):
        plt.plot(y[0],y[1], 'c+')
    k=rrt.closest_point(i)
    plt.plot(k[0],k[1],'go')
    plt.pause(0.1)
    if k==goal:
        print(rrt.path)
        goal_notfound=False
        

plt.show()     


    






