
function modifyString(target: string, input: string, index: number) {
    return target.slice(0, index) + input + target.slice(index + input.length);
}

class Beam {
    constructor(public row: number, public col: number) {}

    key(): string {
        return `${this.row},${this.col}`;
    }
}

type Point = {row: number, col: number};

class Path {
    private _path: Point[];

    constructor(path: Point[]) {
        this._path = path;
    }

    add(point: Point) {
        this._path.push(point);
    }

    clone(): Path {
        return new Path([...this._path]);
    }

    get key() {
        return this._path.map((point) => `${point.row},${point.col}`).join("|");
    }

    get row() {
        return this._path[this._path.length-1].row;
    }

    get col() {
        return this._path[this._path.length-1].col;
    }
}

export function part1(lines: string[]): number {
    const manifold: string[] = [...lines];
    let splitCounter = 0;
    
    // find S
    const startIndex = manifold[0].indexOf("S");

    // init frontier
    const frontier: Beam[] = [];
    const explored = new Set<string>;
    frontier.push(new Beam(1, startIndex));
    
    while (frontier.length > 0) {
        const currentBeam: Beam = frontier.pop()!;

        // check for duplicate beams
        if (!(explored.has(currentBeam?.key()))) {
 
            // add to explored
            explored.add(currentBeam.key());

            // modify manifold
            manifold[currentBeam.row] = modifyString(manifold[currentBeam.row], "|", currentBeam.col);

            // check next step
            if (currentBeam.row + 1 < manifold.length) {
                switch (manifold[currentBeam.row + 1][currentBeam.col]) {
                    case ".":
                        frontier.push(new Beam(currentBeam.row + 1, currentBeam.col));
                        break;

                    case "^":
                        frontier.push(new Beam(currentBeam.row + 1, currentBeam.col - 1));
                        frontier.push(new Beam(currentBeam.row + 1, currentBeam.col + 1));
                        splitCounter += 1;
                }
            } 
        }
    }


    // manifold.forEach((line) => console.log(line));

    return splitCounter;
}

export function part2(lines: string[]): number {
    const manifold: string[] = [...lines];
    // let timelineCounter = 0;
    
    // find S
    const startIndex = manifold[0].indexOf("S");
    const startPoint: Point = {row: 1, col: startIndex};

    // init frontier
    const frontier: Path[] = [];
    const explored = new Set<string>;
    const timelines = new Set<string>;
    frontier.push(new Path([startPoint]));
    
    while (frontier.length > 0) {
        const currentBeam: Path = frontier.pop()!;

        // check for duplicate beams
        if (!(explored.has(currentBeam?.key))) {
 
            // add to explored
            explored.add(currentBeam.key);

            // modify manifold
            // manifold[currentBeam.row] = modifyString(manifold[currentBeam.row], "|", currentBeam.col);

            // if we are not at the ned of the manifold
            if (currentBeam.row + 1 < manifold.length) {

                // check the next step
                switch (manifold[currentBeam.row + 1][currentBeam.col]) {
                    // continue beam
                    case ".":
                        currentBeam.add({row: currentBeam.row + 1, col: currentBeam.col});
                        frontier.push(currentBeam);
                        break;

                    // split beam;
                    case "^":
                        const leftBranch = currentBeam.clone();
                        leftBranch.add({row: currentBeam.row + 1, col: currentBeam.col - 1});
                        frontier.push(leftBranch);

                        const rightBranch = currentBeam.clone();
                        rightBranch.add({row: currentBeam.row + 1, col: currentBeam.col + 1});
                        frontier.push(rightBranch);
                        break;
                }
            } else {
                // end of manifold reached
                timelines.add(currentBeam.key);
            }
        } 
    }


    // manifold.forEach((line) => console.log(line));

    return timelines.size;
}