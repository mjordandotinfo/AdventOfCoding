package main

import (
	"bufio"
	"log"
	"os"
	"regexp"
)

//TIP <p>To run your code, right-click the code and select <b>Run</b>.</p> <p>Alternatively, click
// the <icon src="AllIcons.Actions.Execute"/> icon in the gutter and select the <b>Run</b> menu item from here.</p>

func getCorners(ws []string, row int, col int) (string, string, string, string) {
	var upLeft, downLeft, upRight, downRight string
	upRow := row - 1
	downRow := row + 1
	leftCol := col - 1
	rightCol := col + 1

	if upRow >= 0 && downRow < len(ws) && leftCol >= 0 && rightCol < len(ws[0]) {
		upLeft = ws[upRow][leftCol : leftCol+1]
		upRight = ws[upRow][rightCol : rightCol+1]
		downLeft = ws[downRow][leftCol : leftCol+1]
		downRight = ws[downRow][rightCol : rightCol+1]
	}

	//println(upLeft, upRight, downLeft, downRight)

	return upLeft, downRight, upRight, downLeft
}

func main() {
	file, err := os.Open("input.txt")
	if err != nil {
		log.Fatal(err)
	}
	defer file.Close()

	// build wordsearch
	var wordsearch []string
	scanner := bufio.NewScanner(file)
	for scanner.Scan() {
		line := scanner.Text()
		wordsearch = append(wordsearch, line)
		//println(line)
	}

	//dirs := [8][2]int{
	//	// row, col
	//	// PART 1 {-1, 0},  // UP
	//	// PART 1 {0, 1},   // RIGHT
	//	// PART 1 {1, 0},   // DOWN
	//	// PART 1 {0, -1},  // LEFT
	//	{-1, 1},  // UP-RIGHT
	//	{1, -1},  // DOWN-LEFT
	//	{-1, -1}, // UP-LEFT
	//	{1, 1},   // DOWN-RIGHT
	//}

	// PART 1 re := regexp.MustCompile(`X`)
	re := regexp.MustCompile("A")
	total := 0
	//letters := "MAS"
	for curRow, line := range wordsearch {
		matches := re.FindAllStringIndex(line, -1)
		for _, match := range matches {
			row := curRow
			col := match[0]
			//fmt.Printf("Checking Row: %d, %d\n", curRow, match[0])
			uL, dR, uR, dL := getCorners(wordsearch, row, col)
			one := uL + "A" + dR
			two := uR + "A" + dL
			if (one == "MAS" || one == "SAM") && (two == "MAS" || two == "SAM") {
				total++
			}
			//for _, dir := range dirs {
			//	row := curRow
			//	col := match[0]
			//	for i := 0; i < len(letters); i++ {
			//		row += dir[0]
			//		col += dir[1]
			//		// out of bounds
			//		if row < 0 || col < 0 || row >= len(wordsearch) || col >= len(wordsearch[row]) {
			//			break
			//		}
			//		// letters don't match
			//		if wordsearch[row][col] != letters[i] {
			//			break
			//		}
			//		// SUCCESS!
			//		if i == len(letters)-1 {
			//			total++
			//		}
			//	}
			//}
		}
	}
	println(total)
}
