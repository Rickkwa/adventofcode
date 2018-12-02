package main

import (
	"fmt"
	"io/ioutil"
	"strings"
	"os"
)

func readInput() []string {
	dat, err := ioutil.ReadFile("./input.txt")
	if err != nil {
		panic(err)
	}
	return strings.Fields(strings.Trim(string(dat), "\n"))
}

func countDifferingCharacters(a string, b string) int {
	count := 0
	for index := range a {
		if a[index] != b[index] {
			count++
		}
	}
	return count
}

func main() {
	boxIDs := readInput()

	// Will make the assumption that all IDs are the same length

	for _, id1 := range boxIDs {
		for _, id2 := range boxIDs {
			if id1 == id2 {
				continue
			}

			if countDifferingCharacters(id1, id2) == 1 {
				fmt.Println("First :", id1)
				fmt.Println("Second:", id2)
				fmt.Print("Common: ")
				for index := range id1 {
					if id1[index] == id2[index] {
						fmt.Print(string(id1[index]))
					}
				}
				fmt.Println()
				os.Exit(0)
			}
		}
	}
}
