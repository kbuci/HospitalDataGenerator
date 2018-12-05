import heapq

BARRIER = 2**10
print(type(round(3.4)))
def manhattanDist(x,y):
    return abs(x) + abs(y)
#acc is array of (x,y) for all possible accident sites
#amCount is the number of ambulances
def genAccidentFunc(acc, amCount):
    bounds = [(0,len(acc) - 1) for i in range(amCount)]
    def objectiveFunc(am):
        loc = [(int(round(index))) for index in am]
        repeats = len(loc) - len(set(loc))
        if repeats > 0:
            return BARRIER * repeats**2
        return sum(manhattanDist(acc[index][0], acc[index][1]) for index in loc)       
    return objectiveFunc, bounds #bounds is the limits for each index (used by scipy exponential differential thing)

def optimalSol(acc, amCount):
    accHeap = [(manhattanDist(site[0], site[1]), site[0], site[1]) for site in acc]
    heapq.heapify(accHeap)
    return sum(heapq.heappop(accHeap)[0] for i in range(amCount))
