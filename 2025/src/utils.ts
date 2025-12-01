import { readFileSync } from "fs";
import { join } from "path";

export function readInput(day: string, mode: "real" | "test" = "real"): string {
    const baseFolder = mode === "test" ? "test-inputs" : "inputs";

    const filePath = join(__dirname,
        "..",
        baseFolder,
        `day${day}.txt`
    );

    return readFileSync(filePath, "utf-8").replace(/\r\n/g, "\n").trimEnd();
}

export function readLines(day: string, mode: "real" | "test" = "real"): string[] {
    return readInput(day, mode).split("\n");
}

export function toNumbers(lines: string[]): number[] {
    return lines.map((line) => Number(line));
}