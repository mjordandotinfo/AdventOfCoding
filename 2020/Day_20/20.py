class Tile():
    def read_img(self, img):
        self.edges["top"] = img[0]
        self.edges["bot"] = img[-1]
        self.edges["left"] = ""
        self.edges["right"] = ""
        for line in img:
            self.edges["left"] += line[0]
            self.edges["right"] += line[-1]

    def __init__(self, ID):
        self.id = ID
        self.edges = {}
        self.neighbors = {}

def main():
    f = open("C:/Users/mattr/Documents/Advent-Coding/Day_20/20_input.txt", "r")
    tiles = [x.splitlines() for x in f.read().split("\n\n")]
    D = {}

    for tile in tiles:
        if not tile:
            break
        tileID = int(tile[0][5:-1])
        myTile = Tile(tileID)
        myTile.read_img(tile[1:])
        D[myTile.id] = myTile
    
    for tile in D:
        for edge in D[tile].edges:
            for match in D:
                if match != tile:
                    for match_edge in D[match].edges:
                        if D[tile].edges[edge] == D[match].edges[match_edge]:
                            print(tile, D[tile].edges[edge], edge)
                            print(match, D[match].edges[match_edge], match_edge, "\n")
                            D[tile].neighbors[edge] = match
                            D[match].neighbors[match_edge] = tile
                        elif D[tile].edges[edge][::-1] == D[match].edges[match_edge]:
                            print(tile, D[tile].edges[edge], edge)
                            print(match, D[match].edges[match_edge], match_edge, "\n")
                            D[tile].neighbors[edge] = match
                            D[match].neighbors[match_edge] = tile

    total = 1
    for tile in D:
        if len(D[tile].neighbors) == 2:
            total *= tile
    
    print(total)

    return

if __name__=="__main__":
    main()
