package main

import (
	"bufio"
	"log"
	"os"
	"regexp"
	"sort"
	"strconv"
	//"strconv"
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
		//muls := re.FindAllString(line, -1)
		muls := reMuls.FindAllStringIndex(line, -1)
		dos := reDos.FindAllStringIndex(line, -1)
		donts := reDonts.FindAllStringIndex(line, -1)

		queue := []Pair{}
		var exps [][][]int
		exps = append(exps, muls, dos, donts)
		for _, matches := range exps {
			for _, match := range matches {
				queue = append(queue, Pair{match[0], match[1], line[match[0]:match[1]]})
			}
		}

		// sort the queue
		sort.Slice(queue, func(i, j int) bool {
			return queue[i].start < queue[j].start
		})

		enabled := true
		lineTotal := 0
		for _, match := range queue {
			if match.value == "don't()" {
				enabled = false
				continue
			} else if match.value == "do()" {
				enabled = true
				continue
			}

			// match.value == mul
			//println(match.start, match.value)
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
		//for i, match := range muls {
		//	for j, val := range match {
		//		println(i, j, val, line[match[0]:match[1]])
		//	}
		//}

		//dontRe := regexp.MustCompile("don't\\(\\)")
		//doRe := regexp.MustCompile("do\\(\\)")
		//donts := dontRe.FindAllStringIndex(line, -1)
		//dos := doRe.FindAllStringIndex(line, -1)

		//println(muls)
		//for i, mul := range muls {
		//	println(i, mul[0], mul[1], line[mul[0]:mul[1]])
		//	//nums := numRe.FindAllString(level, -1)
		//	//op1, _ := strconv.Atoi(nums[0])
		//	//op2, _ := strconv.Atoi(nums[1])
		//	//total += op1 * op2
		//}
	}

	//println(total)

	if err := scanner.Err(); err != nil {
		panic(err)
	}
}
