import sys
def greedy_tsp(distances):
    n=len(distances)
    vis=[False]*n
    route=[0] 
    vis[0]=True
    total_dist=0
    for _ in range(1,n):
        last=route[-1]
        nearest=None
        min_dist=float('inf')
        for i in range(n):
            if vis[i]==0 and distances[last][i]<min_dist:
                min_dist=distances[last][i]
                nearest=i
        route.append(nearest)
        vis[nearest]=True
        total_dist+=min_dist 
    total_dist+=distances[last][0]
    return total_dist, route
def inputfile(filename):
    with open(filename, 'r') as f:
        [n]=[int(x) for x in f.readline().split()]
        distances=[]
        for i in range(n):
            row=[int(x) for x in f.readline().split()]
            distances.append(row)
    return n, distances        
def Input():
    f=sys.stdin
    [n]=[int(x) for x in f.readline().split()]
    distances=[]
    for i in range(n):
        row=[int(x) for x in f.readline().split()]
        distances.append(row)
    return n, distances   
#n,distances=inputfile('TSP data.txt')            
n,distances=Input()
total_dist,route=greedy_tsp(distances)
print(n)
for city in route:
    print(city+1, end=' ')  
