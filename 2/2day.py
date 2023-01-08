import fileinput


lines = list(fileinput.input())
results = []
for line in lines:
    results.append(line)


# Part 1
rps_map = { 'A': 'R', 'B': 'P', 'C': 'S', 'X': 'R', 'Y': 'P', 'Z': 'S' }
rps_points = { 'R': 1, 'P': 2, 'S': 3 }
def rps_outcome(opp, me):
    if opp == me:
        return 3
    elif (opp == 'R' and me == 'S') or (opp =='P' and me =='R') or (opp =='S' and me =='P'):
        return 0
    else:
        return 6

points = 0
for line in results:
    opp = rps_map.get(line[0])
    me = rps_map.get(line[2])
    outcome = rps_outcome(opp,me)
    points += outcome + rps_points.get(me)
print(points)

# Part 2
rps_xyz = { 'X': -1, 'Y': 0, 'Z': 1 }
rps_win = { 'R': 'P', 'P': 'S', 'S': 'R' }
rps_lose = { 'R': 'S', 'P': 'R', 'S': 'P' }
rps_draw = { 'R': 'R', 'P': 'P', 'S': 'S' }
points = 0
for line in results:
    opp = rps_map.get(line[0])
    outcome = rps_xyz.get(line[2])
    if outcome == -1:
        me = rps_lose.get(opp)
    elif outcome == 0:
        me = rps_draw.get(opp)
    else:
        me = rps_win.get(opp)
    outcome = rps_outcome(opp,me)
    points += outcome + rps_points.get(me)
print(points)
