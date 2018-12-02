package main

import (
	"fmt"
	"io/ioutil"
	"strings"
)

func readInput() []string {
	dat, err := ioutil.ReadFile("./input.txt")
	if err != nil {
		panic(err)
	}
	return strings.Split(strings.Trim(string(dat), "\n"), "\n")
}

func main() {
	boxIDs := readInput()
	var countTwos, countThrees int = 0, 0
	for _, id := range boxIDs {
		for _, char := range(id) {
			if strings.Count(id, string(char)) == 2 {
				countTwos += 1
				break
			}
		}
		for _, char := range(id) {
			if strings.Count(id, string(char)) == 3 {
				countThrees += 1
				break
			}
		}
	}
	fmt.Println("Twos:", countTwos, "; Threes:", countThrees)
	fmt.Println("Checksum:", (countTwos * countThrees))
}
