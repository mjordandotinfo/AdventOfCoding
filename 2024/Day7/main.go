package main

import (
	"bufio"
	"log"
	"math"
	"os"
	"strconv"
	"strings"
)

//func buildBitMap(bits int, val int) []string {
//	bitmap := make([]string, bits)
//	for i := bits-1; i >= 0; i-- {
//		bit :=
//	}
//}

func concat(a int, b int) int {
	digits := math.Ceil(math.Log10(float64(b)))
	return (a * int(math.Pow10(int(digits)))) + b
}

func operate(target int, currentTotal int, values []int) bool {
	// base case
	if len(values) == 1 {
		if (currentTotal+values[0]) == target || (currentTotal*values[0]) == target || concat(currentTotal, values[0]) == target {
			return true
		} else {
			return false
		}
	}

	// add branch
	if operate(target, currentTotal+values[0], values[1:]) {
		return true
	}

	// multiply branch
	if operate(target, currentTotal*values[0], values[1:]) {
		return true
	}

	// concat branch
	if operate(target, concat(currentTotal, values[0]), values[1:]) {
		return true
	}

	return false
}

func inputStrToInt(input []string) (int, []int) {
	testValue, _ := strconv.Atoi(input[0][0 : len(input[0])-1])
	parsedInt := make([]int, len(input))
	for i, str := range input {
		num, _ := strconv.Atoi(str)
		parsedInt[i] = num
	}
	return testValue, parsedInt[1:]
}

func main() {
	file, err := os.Open("input.txt")
	if err != nil {
		log.Fatal(err)
	}
	defer file.Close()

	total := 0
	scanner := bufio.NewScanner(file)
	for scanner.Scan() {
		line := scanner.Text()
		parsed := strings.Split(line, " ")
		target, values := inputStrToInt(parsed)
		//fmt.Printf("TestValue: %d %v \n", target, values)
		result := operate(target, values[0], values[1:])
		//println(result)
		if result {
			println(line)
			total += target
		}
	}

	println(total)

	if err := scanner.Err(); err != nil {
		return
	}

}
