package main

import (
	"bufio"
	"log"
	"os"
	"strconv"
	"strings"
)

func insert(array []string, from int, to int) []string {
	tempArray := make([]string, len(array))
	copy(tempArray, array)
	// Pop out from value
	if from == len(array)-1 {
		tempArray = tempArray[:len(array)-1]
	} else {
		tempArray = append(tempArray[:from], tempArray[from+1:]...)
	}

	//insert value
	tempArray = append(tempArray[0:to], append(array[from:from+1], tempArray[to:]...)...)

	return tempArray
}

func swap(array []string, i int, j int) []string {
	tempArray := make([]string, len(array))
	copy(tempArray, array)
	tempArray[i] = array[j]
	tempArray[j] = array[i]
	return tempArray
}

func checkRule(rule []string, nums []string) (bool, int) {
	for _, v := range rule {
		i := in(v, nums)
		if i != -1 {
			return false, i
		}
	}
	return true, -1
}

func in(val string, array []string) int {
	for i, v := range array {
		if v == val {
			return i
		}
	}
	return -1
}

func SplitPages(s string, sep string) (string, string) {
	x := strings.Split(s, sep)
	return x[0], x[1]
}

func main() {

	file, err := os.Open("input.txt")
	if err != nil {
		log.Fatal(err)
	}
	defer file.Close()

	scanner := bufio.NewScanner(file)

	// Scan the first half of the input
	rules := make(map[string][]string)
	for scanner.Scan() {
		line := scanner.Text()
		if line == "" {
			break
		}

		before, after := SplitPages(line, "|")
		//println(before, after)
		_, ok := rules[before]
		if !ok {
			rules[before] = []string{after}
		} else {
			rules[before] = append(rules[before], after)
		}
	}

	// Scan the second half of the input
	total := 0
	var brokenPageOrders [][]string
	for scanner.Scan() {
		line := scanner.Text()
		pages := strings.Split(line, ",")
		// iterate backwards over pages
		rulePass := true
		for currentIndex := len(pages) - 1; currentIndex >= 1; currentIndex-- {
			page := pages[currentIndex]
			// check for page in rules list
			rule, ok := rules[page]
			if ok {
				// if any pages to left are in the rule, then fail
				passResult, failedIndex := checkRule(rule, pages[0:currentIndex])
				if !passResult {
					pages = insert(pages, currentIndex, failedIndex)
					rulePass = false
					brokenPageOrders = append(brokenPageOrders, pages)
					currentIndex++
				}

			}
		}
		// Find the midpoint and add to total if fixed
		if !rulePass {
			mid, _ := strconv.Atoi(pages[len(pages)/2])
			total += mid
		}
	}

	println(total)

	if err := scanner.Err(); err != nil {
		panic(err)
	}

}
