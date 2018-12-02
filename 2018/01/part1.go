package main;

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

func main() {
	frequencies := readInput()
	frequencySum := 0

	for _, element := range frequencies {
		fmt.Println(element)
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
	}

	fmt.Println(frequencySum)
}
