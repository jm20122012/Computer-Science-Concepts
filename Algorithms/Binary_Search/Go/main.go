package main

import (
	"log"
)

func binarySearch(array []int, searchTarget int) int {
	log.Printf("Starting Binary Search...")

	var lowIndex int = 0               // Setting the starting low index to 0
	var highIndex int = len(array) - 1 // Setting the starting high index to the last index

	// While the low index is less than or equal to the high index, perform loop
	for lowIndex <= highIndex {
		log.Println("----- Starting loop iteration -----")
		log.Printf("High Index: %d", highIndex)
		log.Printf("Low Index: %d", lowIndex)
		log.Printf("Search array: %v", array[lowIndex:highIndex+1])

		// Get middle index
		var middleIndex int = lowIndex + (highIndex-lowIndex)/2
		log.Printf("Middle Index: %d", middleIndex)

		// Get the value at the middle index
		var value int = array[middleIndex]
		log.Printf("Value at middle index of %d: %d", middleIndex, value)

		// Check if value is less than or greater than the target

		// If value is lower than the target then the target is in the right side portion of the array
		// Set new low index to be the middleIndex + 1 and keep the current high index
		// Else if the value is greater than the target, then the target is in the left side portion of the array
		// Set new high index to be the middleIndex - 1 and keep the current low index
		if value < searchTarget {
			log.Printf("Value %d is less than the target search value %d.  Setting new low index to %d", value, searchTarget, middleIndex+1)
			lowIndex = middleIndex + 1
		} else if value > searchTarget {
			log.Printf("Value %d is greater than the target search value %d.  Setting new high index to %d", value, searchTarget, middleIndex-1)
			highIndex = middleIndex - 1
		} else {
			// If the value is neither less than or greater than the searchTarget, we have found our value
			return middleIndex
		}
	}

	// If the search target was not found, return -1
	return -1

}

func main() {
	var searchTarget int = 3
	var arrayLen int = 10
	var array []int

	for i := 0; i < arrayLen; i++ {
		array = append(array, i)
	}

	var targetIndex int = binarySearch(array, searchTarget)

	if targetIndex == -1 {
		log.Println("Target not found in array")
	} else {
		log.Printf("Target found at index %d", targetIndex)
	}
}
