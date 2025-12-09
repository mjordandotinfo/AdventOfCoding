
function parseInput(lines: string[]) {
    const split = lines.indexOf("");
    const ranges = lines.slice(0, split);
    const ingredients = lines.slice(split+1);

    return { ranges, ingredients };

}

export function part1(lines: string[]) {
    const { ranges, ingredients } = parseInput(lines);

    let availableIngredients = 0;
    ingredients.forEach((ingredient) => {
        for (const range of ranges) {
            const [start, end] = range.split("-");
            if (Number(ingredient) >= Number(start) && Number(ingredient) <= Number(end)) {
                availableIngredients += 1;
                break;
            }
        }
    });

    return availableIngredients;
}


export function part2(lines: string[]) {
    const { ranges, } = parseInput(lines);
    // console.log(ranges);

    const numericalRanges = ranges.map((range) => {
        const [start, end] = range.split("-");
        return [Number(start), Number(end)];
    });

    numericalRanges.sort((a, b) => {
        if (a[0] !== b[0]) return a[0] - b[0];
        return a[1] - b[1];
    });

    // console.log(numericalRanges);
    for (let i = 0; i < numericalRanges.length - 1; i += 1) {
        if (numericalRanges[i][1] >= numericalRanges[i+1][0]) {
            numericalRanges[i][1] = numericalRanges[i+1][1];
            numericalRanges.splice(i+1,1);
            i -= 1;
            // console.log(numericalRanges);
        }
    }

    let numFresh = 0;
    numericalRanges.forEach((range) => {
        numFresh += (range[1] - range[0] + 1);
    })

    // console.log(numFresh);
    return numFresh;
}