from collections import defaultdict


def possiblethrows(onlyDoubles=True):
    ptdict = defaultdict(list)
    for i in range (1,20):
        ptdict[i * 2].append("double " + str(i))
    ptdict[50].append("bullseye 50")
    if not onlyDoubles:
        for i in range(1, 21):
            ptdict[i].append("single " + str(i))
            ptdict[i*3].append("triple " + str(i))
        ptdict[25].append("bull 25")
    return ptdict



def dartboardgame(points=301, startwithdouble=True, endwithdouble=True):
    pta = possiblethrows(onlyDoubles=False)
    ptd = possiblethrows(onlyDoubles=True)
    gameplan = []
    if startwithdouble:
        throw = max([d for d in ptd if d <= points])
        gameplan.append([points, ptd[throw][0]])
        points -= throw
    while points != 0:
        throw = max([d for d in pta if d <= points])
        if endwithdouble:
            if 50 > points < 140:
                throw = max([d for d in pta if points - d % 2 == 0 and d <= points])
            elif points <= 50:
                throw = max([d for d in ptd if d <= points])
                gameplan.append([points, ptd[throw][0]])
        else:
            gameplan.append([points, pta[throw][0]])
        points -= throw
    return gameplan
