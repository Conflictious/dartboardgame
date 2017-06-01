from collections import defaultdict


def possiblethrows():
    ptdict = defaultdict(list)
    for i in range(1,21):
        ptdict[i].append("single " + str(i))
        ptdict[i*2].append("double " + str(i))
        ptdict[i*3].append("triple " + str(i))
    return ptdict

def dartboardgame(points):
    pt = possiblethrows()
    gameplan = []
    while points != 0:
        throw = max([d for d in pt if d <= points])
        #the last throw has to be a double
        if points - throw <= 1 and throw not in range(0,40,2):
            throw = max([d for d in pt if d <= points-2])
            gameplan.append([points,pt[throw][0]])
            points -= throw
        else:
            throw = max([d for d in pt if d <= points])
            gameplan.append([points,pt[throw][0]])
            points -= throw
    return gameplan
    
    
