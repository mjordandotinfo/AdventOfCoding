import { argv, exit } from "process";

function parseDayArg(): string {
    const raw = argv[2];

    if (!raw) {
        console.error("Usage: npm run day -- <dayNumber>");
        exit(1);
    }

    const dayNum = Number(raw);

    if (!Number.isInteger(dayNum) || dayNum < 1 || dayNum > 25) {
        console.error("Day must be an integer between 1 and 25.");
        exit(1);
    }

    return dayNum.toString().padStart(2, "0");
}

async function main() {
    const day = parseDayArg();
    const modulePath = `./days/day${day}`;

    const mod = require(modulePath) as {
        part1?: () => unknown;
        part2?: () => unknown;
    };

    console.log(`Day ${day}`);

    if (typeof mod.part1 === "function") {
        const result1 = mod.part1();
        console.log("Part 1:", result1);
    } else {
        console.log("Part 1: (not implemented)");
    }

    if (typeof mod.part2 === "function") {
        const result2 = mod.part2();
        console.log("Part 2:", result2);
    } else {
        console.log("Part 2: (not implemented)");
    }
}

main();