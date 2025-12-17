
function modifyString(target: string, input: string, index: number) {
    return target.slice(0, index) + input + target.slice(index + input.length);
}

class Beam {
    constructor(public row: number, public col: number) {}

    key(): string {
        return `${this.row},${this.col}`;
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

// export function part2(lines: string[]): number {
//   const nums = lines.map(Number);

//   // Example: product of all numbers
//   return nums.reduce((prod, n) => prod * n, 1);
// }