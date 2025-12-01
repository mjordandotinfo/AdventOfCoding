import { argv, exit } from "process";
import { readLines } from "./utils";

type Mode = "real" | "test";

function parseDayArg(): {day: string; mode: Mode} {
    const rawDay = argv[2];
    const rawMode = argv[3] ?? "real";

    if (!rawDay) {
        console.error("Usage: npm run day -- <dayNumber> [real|test]");
        exit(1);
    }

    const dayNum = Number(rawDay);

    if (!Number.isInteger(dayNum) || dayNum < 1 || dayNum > 25) {
        console.error("Day must be an integer between 1 and 25.");
        exit(1);
    }

    const mode = (rawMode === "test" ? "test" : "real") as Mode;
    const day = dayNum.toString().padStart(2, "0");

    return {day, mode};
}

async function main() {
    const {day, mode} = parseDayArg();
    const modulePath = `./days/day${day}`;

    const mod = require(modulePath) as {
        part1?: (lines: string[]) => unknown;
        part2?: (lines: string[]) => unknown;
    };

    const lines = readLines(day, mode);

    console.log(`Day ${day} (${mode.toUpperCase()} input)`);

    if (typeof mod.part1 === "function") {
        const result1 = mod.part1(lines);
        console.log("Part 1:", result1);
    } else {
        console.log("Part 1: (not implemented)");
    }

    if (typeof mod.part2 === "function") {
        const result2 = mod.part2(lines);
        console.log("Part 2:", result2);
    } else {
        console.log("Part 2: (not implemented)");
    }
}

main();