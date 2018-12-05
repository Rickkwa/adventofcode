package main

import (
	"fmt"
	"io/ioutil"
	"strings"
	"strconv"
)

func readInput() []string {
	dat, err := ioutil.ReadFile("./input.txt")
	if err != nil {
		panic(err)
	}
	return strings.Split(strings.Trim(string(dat), "\n"), "\n")
}

func toInt(s string) int {
	result, err := strconv.Atoi(s)
	if err != nil {
		panic(err)
	}
	return result
}

func check(grid map[int]map[int]int, leftOffset, topOffset, leftLength, topLength int) bool {
	for i := leftOffset; i < leftOffset + leftLength; i++ {
		for j := topOffset; j < topOffset + topLength; j++ {
			if grid[i][j] > 1 {
				return false
			}
		}
	}
	return true
}

func main() {
	lines := readInput()

	grid := make(map[int]map[int]int)

	for _, line := range lines {
		tokens := strings.Split(line, " ")
		leftOffset := toInt(strings.Split(strings.Trim(tokens[2], ":"), ",")[0])
		topOffset := toInt(strings.Split(strings.Trim(tokens[2], ":"), ",")[1])

		leftLength := toInt(strings.Split(tokens[3], "x")[0])
		topLength := toInt(strings.Split(tokens[3], "x")[1])

		for i := leftOffset; i < leftOffset + leftLength; i++ {
			for j := topOffset; j < topOffset + topLength; j++ {
				if grid[i] == nil {
					grid[i] = make(map[int]int)
				}
				grid[i][j]++
			}
		}
	}


	for _, line := range lines {
		tokens := strings.Split(line, " ")
		leftOffset := toInt(strings.Split(strings.Trim(tokens[2], ":"), ",")[0])
		topOffset := toInt(strings.Split(strings.Trim(tokens[2], ":"), ",")[1])
		leftLength := toInt(strings.Split(tokens[3], "x")[0])
		topLength := toInt(strings.Split(tokens[3], "x")[1])

		if !check(grid, leftOffset, topOffset, leftLength, topLength) {
			continue
		}
		fmt.Println(tokens[0])
	}
}
