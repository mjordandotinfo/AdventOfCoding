// src/days/day01.ts
import { readFileSync } from "fs";
import { join } from "path";

function getInput(): string {
  const filePath = join(__dirname, "..", "..", "inputs", "day01.txt");
  return readFileSync(filePath, "utf-8").trim();
}

export function part1(): number {
  const data = getInput()
    .split("\n")
    .map(Number);

  // Example: sum all numbers
  return data.reduce((sum, n) => sum + n, 0);
}

export function part2(): number {
  const data = getInput()
    .split("\n")
    .map(Number);

  // Example: product of all numbers
  return data.reduce((prod, n) => prod * n, 1);
}
