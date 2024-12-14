package main

import (
	"bufio"
	"log"
	"os"
	"strings"
)

type coord struct {
	x int
	y int
}

func checkObstacle(puzzle [][]string, pos coord) bool {
	if puzzle[pos.y][pos.x] == "#" {
		return true
	} else {
		return false
	}
}

func step(pos coord, dir coord) coord {
	return coord{pos.x + dir.x, pos.y + dir.y}
}

func checkBounds(puzzle [][]string, pos coord) bool {
	// [Y][X]
	if pos.x >= len(puzzle[0]) || pos.y >= len(puzzle) || pos.x < 0 || pos.y < 0 {
		return false
	} else {
		return true
	}
}

func rotate(dir coord) coord {
	up := coord{0, -1}
	down := coord{0, 1}
	left := coord{-1, 0}
	right := coord{1, 0}

	switch dir {
	case up:
		return right
	case right:
		return down
	case down:
		return left
	case left:
		return up
	default:
		return dir
	}
}

func main() {
	file, err := os.Open("input.txt")
	if err != nil {
		log.Fatal(err)
	}
	defer file.Close()

	var puzzle [][]string

	pos := coord{0, 0}
	scanner := bufio.NewScanner(file)
	y := 0
	for scanner.Scan() {
		line := scanner.Text()
		var chars []string
		for _, char := range line {
			chars = append(chars, string(char))
		}
		puzzle = append(puzzle, chars)
		index := strings.Index(line, "^")
		if index != -1 {
			pos.x = index
			pos.y = y
		}
		y++
	}

	steps := 0
	inbounds := true
	dir := coord{0, -1} // UP
	for inbounds {
		// Check next
		if checkBounds(puzzle, step(pos, dir)) {
			if checkObstacle(puzzle, step(pos, dir)) {
				dir = rotate(dir)
				continue
			}
		} else {
			inbounds = false
		}
		if puzzle[pos.y][pos.x] != "X" {
			puzzle[pos.y][pos.x] = "X"
			steps++
		}
		pos = step(pos, dir)
	}

	println(steps)

	if err := scanner.Err(); err != nil {
		panic(err)
	}
}
