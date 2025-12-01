// src/days/day01.ts
// import { readFileSync } from "fs";
// import { join } from "path";

// function getInput(): string {
//   const filePath = join(__dirname, "..", "..", "inputs", "day01.txt");
//   return readFileSync(filePath, "utf-8").trim();
// }

export function part1(lines: string[]): number {
  const nums = lines.map(Number);

  // Example: sum all numbers
  return nums.reduce((sum, n) => sum + n, 0);
}

export function part2(lines: string[]): number {
  const nums = lines.map(Number);

  // Example: product of all numbers
  return nums.reduce((prod, n) => prod * n, 1);
}
