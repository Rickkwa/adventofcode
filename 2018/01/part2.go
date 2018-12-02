package main;

import (
	"fmt"
	"io/ioutil"
	"strings"
	"strconv"
	"os"
)

func readInput() []string {
	dat, err := ioutil.ReadFile("./input.txt")
	if err != nil {
		panic(err)
	}
	return strings.Split(strings.Trim(string(dat), "\n"), "\n")
}

func inArrayInt(x int, xs []int) bool {
	for _, el := range xs {
		if x == el {
			return true
		}
	}
	return false
}

func main() {
	frequencies := readInput()
	frequencySum := 0
	var seen []int

	i := 0

	for true {
		element := frequencies[i]
		i = (i + 1) % len(frequencies)

		n, convErr := strconv.Atoi(strings.Replace(element, string(element[0]), "", -1))
		if convErr != nil {
			panic(convErr)
		}

		if string(element[0]) == "+" {
			frequencySum += n
		} else if string(element[0]) == "-" {
			frequencySum -= n
		} else {
			fmt.Printf("Frequency invalid format: %s\n", element)
		}

		if inArrayInt(frequencySum, seen) {
			fmt.Println("DONE")
			fmt.Println(frequencySum)
			os.Exit(0)
		} else {
			seen = append(seen, frequencySum)
		}
	}

	fmt.Println(seen)
	fmt.Println("None")
}
