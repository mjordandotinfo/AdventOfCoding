function parseInputs(line: string): {sign: number, val: number} {
    const sign = line.charAt(0) === "R" ? 1 : -1;
    const val = Number(line.slice(1));

    return {sign, val}
}

export function part1(lines: string[]): number {
    let dial = 50;
    let password = 0;
    
    for (const line of lines) {
        const {sign, val} = parseInputs(line);
        dial += sign * val;

        if (dial % 100 == 0) {
            password += 1;
        }
    }

  return password;
}

export function part2(lines: string[]): number {
    let dial = 50;
    let password = 0;

    for (const line of lines) {
        let { sign, val } = parseInputs(line); // sign: 1 for R, -1 for L

        // count full 100-step revolutions
        const revolutions = Math.floor(val / 100);
        password += revolutions;
        val -= revolutions * 100; 

        // apply the leftover movement
        const newDialRaw = dial + (sign * val);

        // check if this leftover movement crosses the boundary
        if (sign === 1 && dial + val >= 100) {
            // moved right past 99 to 0
            password += 1;
        } else if (sign === -1 && dial - val < 0) {
            // moved left past 0 to 99
            password += 1;
        }

        // Wrap dial into [0, 99]
        dial = ((newDialRaw % 100) + 100) % 100;
        console.log(dial);
    }

    return password;
}