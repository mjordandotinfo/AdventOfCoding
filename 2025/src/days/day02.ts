function parseInputs(lines: string[]){
    return lines[0].split(',').map(range => { 
        return range.split('-').map(num => +num)
    });
}

export function part1(lines: string[]){
    // Part 1 learned from https://github.com/darrenortiz77/aoc/blob/main/src/2025/02/p1.ts

    if (!lines[0]) {
        throw new Error("Input is empty — expected at least one line.");
    }

    // parse input by commas
    const ranges = parseInputs(lines);
    
    // iterate over input ranges
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

export function part2(lines: string[]){
    if (!lines[0]) {
        throw new Error("Input is empty — expected at least one line.");
    }

    // parse input by commas
    const ranges = parseInputs(lines);

    // iterate over input ranges
    let sum = 0;
    const invalidSet = new Set();

    ranges.forEach(([start, end]) => {
        // iterate over every number start to finnish
        for (let cur = start; cur <= end; cur++){
            const curStr = `${cur}`;
            
            // iterate over all possible patterns
            for (let patternLength = 1; patternLength <= curStr.length/2; patternLength++){
                // check that the length is cleanly divisible by the pattern length
                if (curStr.length % patternLength == 0){
                    const patternCount = curStr.length / patternLength;
                    const pattern = curStr.substring(0, patternLength);
                    const re = new RegExp(`^(?:${pattern}){${patternCount}}$`);
                    const match = re.test(curStr);

                    if (match) {
                        // console.log(cur);
                        invalidSet.add(cur);
                    }
                }
            }
        }
    });

    for (const item of invalidSet) {
        sum += Number(item);
    }
    return sum;
}