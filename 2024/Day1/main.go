package main

import (
	"bufio"
	"log"
	"os"
	"sort"
	"strconv"
	"strings"
)

//TIP <p>To run your code, right-click the code and select <b>Run</b>.</p> <p>Alternatively, click
// the <icon src="AllIcons.Actions.Execute"/> icon in the gutter and select the <b>Run</b> menu item from here.</p>

func main() {
	file, err := os.Open("input.txt")
	if err != nil {
		log.Fatal(err)
	}
	defer file.Close()

	scanner := bufio.NewScanner(file)

	var l []int
	var r []int
	var appears = make(map[int]int)

	for scanner.Scan() {
		line := scanner.Text()
		words := strings.Fields(line)
		i, _ := strconv.Atoi(words[0])
		l = append(l, i)
		i, _ = strconv.Atoi(words[1])
		r = append(r, i)
		appears[i] += 1
	}

	if err := scanner.Err(); err != nil {
		panic(err)
	}

	sort.Sort(sort.IntSlice(l))
	//fmt.Println(l)
	sort.Sort(sort.IntSlice(r))
	//fmt.Println(r)

	// Part 1
	//total := 0
	//for i := 0; i < len(l); i++ {
	//	diff := l[i] - r[i]
	//	if diff < 0 {
	//		diff = diff * -1
	//	}
	//	total += diff
	//}
	//fmt.Println(total)

	// Part 2
	total := 0
	for i := 0; i < len(l); i++ {
		//fmt.Printf("%d: %d\n", l[i], appears[l[i]])
		total += l[i] * appears[l[i]]
	}
	println(total)
}
