from ortools.linear_solver import pywraplp
import sys
def Input():
    f=sys.stdin
    [n]=[int(x) for x in f.readline().split()]
    C=[]
    for i in range(n):
        row=[int(x) for x in f.readline().split()]
        C.append(row)
    return n,C
def inputfile(filename):
    with open(filename, 'r') as f:
        [n]=[int(x) for x in f.readline().split()]
        C=[]
        for i in range(n):
            row=[int(x) for x in f.readline().split()]
            C.append(row)
    return n,C
n,C=Input()          
def CreateInitialModel():
    solver=pywraplp.Solver.CreateSolver('SCIP')
    x={}
    for i in range(n):
        for j in range(n):
            if i!=j:
                x[i,j]=solver.IntVar(0,1,'x['+str(i)+','+str(j)+']')
    #Flow balance
    for i in range(n):
        c1=solver.Constraint(1,1)
        for j in range(n):
            if j!=i:
                c1.SetCoefficient(x[i,j],1)
        c2=solver.Constraint(1,1)
        for j in range(n):
            if j!=i:
               c2.SetCoefficient(x[j,i],1)
    return solver,x
def FindNext(i,sx):
    for j in range(n):
        if i!=j and sx[i][j]>0:
            return j
    return -1
def ExtractSubTour(sx):
    cur=0
    ST=[]
    vis=[False for _ in range(n)]
    while True:
        ST.append(cur)
        vis[cur]=True
        cur=FindNext(cur,sx)
        if vis[cur]:
            break
    return ST
def SolveModel():
    global obj
    solver,x=CreateInitialModel()
    for S in SECs:
        c=solver.Constraint(0,len(S)-1)
        for i in S:
            for j in S:
                if i!=j:
                    c.SetCoefficient(x[i,j],1)
    obj=solver.Objective()
    for i in range(n):
        for j in range(n):
            if i!=j:
                obj.SetCoefficient(x[i,j], C[i][j])
    obj.SetMinimization()
    status=solver.Solve()
    #print('Obj = ', int(solver.Objective().Value()))
    s=[[0 for j in range(n)] for i in range(n)]
    for i in range(n):
        for j in range(n):
            if i!=j:
                s[i][j]=x[i,j].solution_value()
    return s, int(solver.Objective().Value())
def AddSEC(C):
    SECs.append(C)
SECs=[]  #global
solver,x=CreateInitialModel()
while True:
    sx, cost=SolveModel()
    ST=ExtractSubTour(sx)
    #print('Detect subtour: ', ST, 'length = ', len(ST))
    if len(ST)==n:
        #print('Optimality found.')
        print(cost)
        break
    AddSEC(ST)
        

