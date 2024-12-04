package main

import (
	"bufio"
	"log"
	"os"
	"regexp"
	"sort"
	"strconv"
)

// I wanted a Tuple-like structure to sort by
type Pair struct {
	start int
	end   int
	value string
}

func main() {
	file, err := os.Open("input.txt")
	if err != nil {
		log.Fatal(err)
	}
	defer file.Close()

	reMuls := regexp.MustCompile("mul\\(\\d{1,3},\\d{1,3}\\)")
	reDos := regexp.MustCompile("do\\(\\)")
	reDonts := regexp.MustCompile("don't\\(\\)")
	reNums := regexp.MustCompile("\\d{1,3}")
	scanner := bufio.NewScanner(file)

	total := 0
	// For each line of input
	for scanner.Scan() {
		line := scanner.Text()
		println(line)

		// Find all Dos, Don't, and Muls
		muls := reMuls.FindAllStringIndex(line, -1)
		dos := reDos.FindAllStringIndex(line, -1)
		donts := reDonts.FindAllStringIndex(line, -1)

		// Add them all to the queue
		queue := []Pair{}
		var exps [][][]int
		exps = append(exps, muls, dos, donts)
		for _, matches := range exps {
			for _, match := range matches {
				queue = append(queue, Pair{match[0], match[1], line[match[0]:match[1]]})
			}
		}

		// sort the queue by index
		sort.Slice(queue, func(i, j int) bool {
			return queue[i].start < queue[j].start
		})

		// default to counting
		enabled := true
		lineTotal := 0
		for _, match := range queue {
			// disable if the queue pulls a don't
			if match.value == "don't()" {
				enabled = false
				continue
				// re-enable if the queue pulls a do
			} else if match.value == "do()" {
				enabled = true
				continue
			}

			// match.value == mul
			// Do the math if a mul and enabled
			if enabled {
				nums := reNums.FindAllString(line[match.start:match.end], -1)
				op1, _ := strconv.Atoi(nums[0])
				op2, _ := strconv.Atoi(nums[1])
				lineTotal += op1 * op2
			}
			println(lineTotal)
		}
		total += lineTotal

		println(total)
	}

	// I don't know why I do this, but chatGPT says I should
	if err := scanner.Err(); err != nil {
		panic(err)
	}
}
