from collections import defaultdict


def possiblethrows():
    dict = defaultdict(list)
    for i in range(1,21):
        dict[i].append("single " + str(i))
        dict[i*2].append("double " + str(i))
        dict[i*3].append("triple " + str(i))

    return dict

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

print(dartboardgame(301))
