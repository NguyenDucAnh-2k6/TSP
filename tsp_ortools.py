import sys
from ortools.constraint_solver import pywrapcp
from ortools.constraint_solver import routing_enums_pb2


def Input():
    [n] = [int(x) for x in sys.stdin.readline().split()]
    C = []
    for _ in range(n):
        row = [int(x) for x in sys.stdin.readline().split()]
        C.append(row)
    return n, C
def inputfile(filename):
    with open(filename,'r') as f:
        [n] = [int(x) for x in f.readline().split()]
        C = []
        for _ in range(n):
           row = [int(x) for x in f.readline().split()]
           C.append(row)
    return n, C
def SolveTSP(n, C):
    manager = pywrapcp.RoutingIndexManager(n,1,0)     #Index utilities
    routing = pywrapcp.RoutingModel(manager)    #Model

    def distance_callback(from_index, to_index):
        from_node = manager.IndexToNode(from_index)
        to_node = manager.IndexToNode(to_index)
        return C[from_node][to_node]

    transit_callback_index = routing.RegisterTransitCallback(distance_callback)    #So as to use the model, register distance_callback
    routing.SetArcCostEvaluatorOfAllVehicles(transit_callback_index)   #Set evaluator from-to using evaluator index

    search_parameters = pywrapcp.DefaultRoutingSearchParameters()
    search_parameters.first_solution_strategy = (
        routing_enums_pb2.FirstSolutionStrategy.PATH_CHEAPEST_ARC     #Heuristic to find first sol
    )
    search_parameters.local_search_metaheuristic = (
        routing_enums_pb2.LocalSearchMetaheuristic.GUIDED_LOCAL_SEARCH
    )
    search_parameters.time_limit.seconds = (
        15  
    )
    #Declare solving
    solution = routing.SolveWithParameters(search_parameters)

    if solution:
        index = routing.Start(0)
        tour = []
        while not routing.IsEnd(index):
            tour.append(manager.IndexToNode(index))
            index = solution.Value(routing.NextVar(index))
        return tour
    else:
        return []


def main():
    #n, C = Input()
    n,C=inputfile('TSP data.txt')
    tour = SolveTSP(n, C)
    print(n)
    print(" ".join(str(i + 1) for i in tour))  


if __name__ == "__main__":
    main()
