class Point {
    x: number;
    y: number;
    key: string;

    constructor(x: number, y:number) {
        this.x = x;
        this.y = y;
        this.key = `${x},${y}`;
    }

    isAdjacent(other: Point): boolean {
        const xmin = this.x - 1;
        const xmax = this.x + 1;
        const ymin = this.y - 1;
        const ymax = this.y + 1;

        if (other.x >= xmin && other.x <= xmax && other.y >= ymin && other.y <= ymax){
            return true;
        }
        
        return false;
    }

    getAdjacent(xUpperBound: number, yUpperBound: number) {
        const adjacentPoints: Point[] = [];
        const xmin = this.x - 1;
        const xmax = this.x + 1;
        const ymin = this.y - 1;
        const ymax = this.y + 1;
        for (let x = xmin; x <= xmax; x++){
            for (let y = ymin; y <= ymax; y++){
                if (x >= 0 && x < xUpperBound && y >= 0 && y < yUpperBound && !(x == this.x && y == this.y)) {
                    adjacentPoints.push(new Point(x, y));
                }
            }
        }

        return adjacentPoints;
    }
}

export function part1(lines: string[]) {
    const rollMap = new Map<string, number>();
    let validRolls = 0;
    for (let y = 0; y < lines.length; y ++) {
        const line = lines[y];
        for (let x = 0; x < line.length; x++){
            if (line[x] == '@') {
                const currentPoint = new Point(x, y);
                // add the point to the Map
                if (!rollMap.has(currentPoint.key)){
                    rollMap.set(currentPoint.key, 0);
                }

                // check for adjacent rolls in the map
                const adjacentPoints = currentPoint.getAdjacent(line.length, lines.length);

                adjacentPoints.forEach((adjacentPoint) => {
                    if (lines[adjacentPoint.y][adjacentPoint.x] == '@') {
                        rollMap.set(currentPoint.key, (rollMap.get(currentPoint.key) ?? 0) + 1);
                    }
                });

            }
        }
    }

    // check for valid rolls
    for (const value of rollMap.values()) {
        if (value < 4) {
            validRolls += 1;
        }
    }

    return validRolls;

}

// export function part2(lines: string[]) {

// }