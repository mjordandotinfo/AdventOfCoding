
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


// export function part2(lines: string[]) {


// }