from itertools import product

testdata = """\
.###..#.
##.##...
....#.#.
#..#.###
...#...#
##.#...#
#..##.##
#.......
"""

#cube2 = read_data(testdata, 2)
def read_data(data, dim):
    D = {}                                               #create dictionary D to hold all points
    for y, row in enumerate(reversed(testdata.split())): #splits input by line, reverses to make origin bottom left
        for x, val in enumerate(row):                    #enumerates rows
            coords = [x, y] + [0] * (dim - 2)            #make x and y coordinates plus an extra 0 per dimension over 2
            D[tuple(coords)] = val                       #typecast coords list to tuple, use as key in dictionary
    return D

def make_deltas(dim):
    origin = tuple([0] * dim)                                          #make an empty tuple for comparison against origin (SW corner)
    return [x for x in product((-1, 0, 1), repeat=dim) if x != origin] #gets all possible deltas to calculate neighbors
                                                                       #repeat is repeatin (-1, 0, 1) for each dimension
                                                                       #comparision to origin makes sure you don't check for yourself

def next_coords(D):
    keys = list(D) #convert cube dictionary to list - this drops values but keeps the coord keys
    #print(keys)
    dim = len(keys[0]) #0 is arbitray, just find the length of a coord to know how many dimensions
    ranges = []
    for d in range(dim):
        a = min(x[d] for x in keys) - 1 #find min in each dimensions, subtract 1 to grow the space
                                        #x[d] represents the coordinate[d] for d = dimensio.
                                        #so iterating through all the points and finding the lowest value in each dimension
        z = max(x[d] for x in keys) + 2 #find max in all dimensions, add 2 since value will be used in range()
        ranges.append(range(a, z))
    return product(*ranges) #multipling each dimension by the range from lowest to highest values creates your new searchable space
                                #returns the iterable for the list of all points in the new space

def add_tuples(a, b):
    #print(a, b)
    return tuple(x + y for (x, y) in zip(a, b)) #returns the neighbor for each key

def apply_deltas(key, deltas):
    #print(key)
    #print(deltas)
    return (add_tuples(key, d) for d in deltas) #returns an iterator sending a key, delta pair to add_tuples

def cycle(cube):
    deltas = make_deltas(len(next(iter(cube)))) #get all possible neighbor deltas
    D = {} #make new dictionary to store updated values
    for key in next_coords(cube): #iterate through each "key", which is a new coordinate after expanding space in all directions
        val = cube.get(key, '.')  #get the value of each corrdinate, if the coordinate doesn't yet exist in dict then return "."
        active_nabe_count = 0     #num of active neighbors
        
        #this loop will get active neighbors for each key
        for neighbor in apply_deltas(key, deltas): #iterate through all neighbors for every key
            neighbor_val = cube.get(neighbor) #get the val of the neighbor, if it doesn't exist returns none
            if neighbor_val == "#": #we only care if neighbors are activated
                active_nabe_count += 1

        #if active check rule
        if val == "#":
            if active_nabe_count in [2, 3]:
                D[key] = "#"
            else:
                D[key] = "."
        
        #else apply inactive rule
        else:
            if active_nabe_count == 3:
                D[key] = "#"
            else:
                D[key] = "."
    
    return D #returns updated cube


cube3 = read_data(testdata, 4)
for _ in range(6): # ' _ ' is a throwaway variable in this context, iterate to 6 for the number of cycles
    cube3 = cycle(cube3)

#print(cube3)
print(sum(v == "#" for v in cube3.values())) #iterable of all valyes in dictionary, sum true for activated values