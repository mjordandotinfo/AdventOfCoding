package main

import (
	"bufio"
	"log"
	"os"
	"strconv"
	"strings"
)

func RemoveIndex(s []string, index int) []string {
	ret := make([]string, 0)
	ret = append(ret, s[:index]...)
	return append(ret, s[index+1:]...)
}

func IsSafe(s []string) bool {
	ascending := 1
	cur, _ := strconv.Atoi(s[0])
	next, _ := strconv.Atoi(s[1])
	if cur > next {
		ascending = -1
	}

	isSafe := true
	for index, _ := range s[:len(s)-1] {
		// ascending: level - prev should be positive
		next, _ = strconv.Atoi(s[index+1])
		result := (next - cur) * ascending

		// ascending flopped or out of tolerance
		if result <= 0 || result > 3 {
			isSafe = false
			break
		}

		cur = next
	}

	return isSafe
}

func main() {
	file, err := os.Open("input.txt")
	if err != nil {
		log.Fatal(err)
	}
	defer file.Close()

	safeCounter := 0

	scanner := bufio.NewScanner(file)
	for scanner.Scan() {
		line := scanner.Text()
		levels := strings.Fields(line)

		// Check for safe before removals
		if IsSafe(levels) {
			safeCounter++
		} else {
			// start removing levels and trying again
			for i, _ := range levels {
				newLevel := RemoveIndex(levels, i)
				if IsSafe(newLevel) {
					safeCounter++
					break
				}
			}
		}
	}
	println(safeCounter)

	if err := scanner.Err(); err != nil {
		panic(err)
	}
}
