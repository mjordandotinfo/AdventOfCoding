export function part1(lines: string[]){
    // Part 1 learned from https://github.com/darrenortiz77/aoc/blob/main/src/2025/02/p1.ts

    if (!lines[0]) {
        throw new Error("Input is empty — expected at least one line.");
    }

    // parse input by commas
    const ranges = lines[0].split(',').map(range => { 
        return range.split('-').map(num => +num)
    });
    
    // loop over input ranges
    let sum = 0;
    ranges.forEach(([start, end]) => {
        // for each range loop from min to max
        for (let cur=start; cur <= end; cur++) {
            const curStr = `${cur}`;
            const halfLength = curStr.length/2;

            // if first half of string is equal to second half of string
            if (curStr.substring(0, halfLength) === curStr.substring(halfLength)){
                sum += cur;
            }
        }
    });

    return sum;
}

export function part2(){

}