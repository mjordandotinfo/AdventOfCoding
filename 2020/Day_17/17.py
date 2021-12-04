import copy

#pocket = {
    #z dimesion
    #z: {
    #   y: {
    #       x: }}
#}

#read file
f = open("C:/Users/mattr/Documents/Advent-Coding/Day_17/test.txt", "r")
myList = [x for x in f.read().splitlines()]
f.close()

#initialize
allSpace = [
    [0,0], #z
    [0,len(myList)-1], #y
    [0,len(myList[1])-1] #x
]

searchSpace = [
    [0,0], #z
    [0,len(myList)-1], #y
    [0,len(myList[1])-1] #x
]

def expand_pocket():
    global allSpace
    [[zmin, zmax], [ymin, ymax], [xmin, xmax]] = allSpace

    #top/bot z
    pocket[zmax] = {}
    pocket[zmin] = {}
    for y in range(ymin,ymax+1):
        pocket[zmax][y] = {}
        pocket[zmin][y] = {}
        for x in range(xmin,xmax+1):
            pocket[zmax][y][x] = "."
            pocket[zmin][y][x] = "."

    #in between
    for z in range(zmin+1,zmax):
        for y in range(ymin,ymax+1):
            if y == ymin or y == ymax:
                pocket[z][y] = {}
                for x in range(xmin,xmax+1):
                    pocket[z][y][x] = "."
            else:
                pocket[z][y][xmin] = "."
                pocket[z][y][xmax] = "."

    allSpace = [[zmin, zmax], [ymin, ymax], [xmin, xmax]]

def print_pocket():
    global allSpace
    for z in range(allSpace[0][0],allSpace[0][1]+1):
        print("\nZ=",z)
        for y in range(allSpace[1][0],allSpace[1][1]+1):
            mystr = ""
            for x in range(allSpace[2][0],allSpace[2][1]+1):
                mystr += pocket[z][y][x]
            print(mystr)
            
def check_space(z,y,x):
    for r in x_range:
        if r == x:
            expand_pocket()

    for r in y_range:
        if r == y:
            expand_pocket()

    for z in z_range:
        if r == z:
            expand_pocket()

    active = 0
    for i in range(z-1,z+2):
        for j in range(y-1,y+2):
            for k in range(x-1,x+2):
                if pocket[i][j][k] == "#" and [i, j, k] != [z, y, x]:
                    active += 1

    if pocket[i][j][k] == "#" and not active in [2, 3]:
        return "."
    elif pocket[i][j][k] == "1" and active == 3:
        return "#"

    return 0

#init pocket
pocket = {0: {}}
for y in range(len(myList)):
    pocket[0][y] = {}
    for x in range(len(myList[y])):
        pocket[0][y][x] = myList[y][x]

print_pocket()
expand_pocket()
expand_pocket()
print_pocket()

""" myCopy = copy.deepcopy(pocket)
zmin, zmax = z_range
ymin, ymax = y_range
xmin, xmax = x_range
#check current space
for z in range(zmin,zmax+1):
    for y in range(ymin,ymax+1):
        for x in range(xmin,xmax+1):
            myCopy[z,y,x] = search_space(z,y,x)

pocket = copy.deepcopy(myCopy)

print_pocket() """
#new cycle
#expand pocket by 1 in all directions
#check current range 
#expand range

