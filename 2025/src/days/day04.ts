
class Point {
    x: number;
    y: number;
    key: string;

    constructor(x: number, y:number) {
        this.x = x;
        this.y = y;
        this.key = `${x},${y}`;
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

function getValidRolls(rollMap: Map<string, Set<string>>) {
    let validRolls: string[] = [];
    rollMap.forEach((rollSet, key) => {
        if (rollSet.size < 4) {
            validRolls.push(key);
        }
    });

    return validRolls
}

export function part2(lines: string[]) {

    const rollMap = new Map<string, Set<string>>();
    
    for (let y = 0; y < lines.length; y ++) {
        const line = lines[y];
        for (let x = 0; x < line.length; x++){
            if (line[x] == '@') {
                const currentPoint = new Point(x, y);
                // add the point to the Map
                if (!rollMap.has(currentPoint.key)){
                    rollMap.set(currentPoint.key, new Set<string>);
                }

                // check for adjacent rolls in the map
                const adjacentPoints = currentPoint.getAdjacent(line.length, lines.length);

                // add each adjacent roll to the set
                adjacentPoints.forEach((adjacentPoint) => {
                    if (lines[adjacentPoint.y][adjacentPoint.x] == '@') {
                        rollMap.get(currentPoint.key)?.add(adjacentPoint.key);
                    }
                });

            }
        }
    }

    // check for valid rolls
    let validRolls = getValidRolls(rollMap);
    let removedRolls = 0;
    while (validRolls.length) {
        validRolls.forEach((rollKey) => {
            // remove roll from Map
            rollMap.delete(rollKey);
            removedRolls += 1;

            // remove roll from other rolls' neihbors
            for (const rolls of rollMap.values()){
                rolls.delete(rollKey);
            }
        })
        validRolls = getValidRolls(rollMap);
    }


    return removedRolls;

}