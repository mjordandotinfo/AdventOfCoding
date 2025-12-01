import { readFileSync } from "fs";
import { join } from "path";

export function readInput(day: string): string {
    const filePath = join(__dirname, "..", "..", "inputs", `day${day}.txt`);
    return readFileSync(filePath, "utf-8").replace(/\r\n/g, "\n").trimEnd();
}

export function readLines(day: string): string[] {
    return readInput(day).split("\n");
}

export function toNumbers(lines: string[]): number[] {
    return lines.map((line) => Number(line));
}