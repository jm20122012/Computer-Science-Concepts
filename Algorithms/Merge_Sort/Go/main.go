package main

import (
	"log"
	"math/rand"
)

func mergeSort(array []int, branch string, sortIteration int) {
	log.Printf("------- Starting Merge Sort on branch %s Iteration %d--------", branch, sortIteration)
	log.Println("Passed Array: ", array)

	// Get the length of the array
	var arrayLength int = len(array)

	// Base case - is length of array is less than or equal to 1, return
	if arrayLength <= 1 {
		log.Println("Array is length 1 - returning")
		return
	}

	// Get the middle of the array
	var arrayMiddleIndex int = arrayLength / 2

	// Create the two sub arrays
	var leftArray = make([]int, 0, arrayMiddleIndex)              // Create left array of size equal to what the middle is
	var rightArray = make([]int, 0, arrayLength-arrayMiddleIndex) // Create right array using the difference between middle and length

	// Create variables for iterating over each sub array
	var i int // leftArray
	var j int // right array

	// Loop over left array and assign elements 0 to array[arrayMiddleIndex] of array to leftArray
	for i = 0; i < arrayMiddleIndex; i++ {
		leftArray = append(leftArray, array[i])
	}

	// Loop over right array and assign elements arrayMiddleIndex to arrayLength of array to leftArray
	for j = arrayMiddleIndex; j < arrayLength; j++ {
		rightArray = append(rightArray, array[j])
	}

	log.Println("Left Array: ", leftArray)
	log.Println("Right Array: ", rightArray)
	// Now recursively call mergeSort until arrays are divided into lengths of 1
	sortIteration += 1
	mergeSort(leftArray, "left", sortIteration)
	log.Println("Left mergeSort complete - Starting right mergeSort")
	mergeSort(rightArray, "right", sortIteration)
	log.Println("Right mergeSort complete - Starting merge function")

	log.Printf("Passing leftArray %v to merge", leftArray)
	log.Printf("Passing rightArray %v to merge", rightArray)
	log.Printf("Passing array %v to merge", array)
	merge(leftArray, rightArray, array)
}

func merge(leftArray []int, rightArray []int, array []int) {
	log.Println("------- Starting MERGE function -------")
	log.Printf("leftArray: %v - rightArray: %v, array: %v", leftArray, rightArray, array)
	leftArrLen := len(leftArray)
	rightArrLen := len(rightArray)
	var i int
	var l int
	var r int

	log.Println("Running loop while l is less than leftArray length, and r is less than rightArray length")
	for l < leftArrLen && r < rightArrLen {
		log.Printf("l value: %d - r value: %d", l, r)
		if leftArray[l] < rightArray[r] {
			log.Printf("leftArray index %d with data %d is less than rightArray index %d with data %d", l, leftArray[l], r, rightArray[r])
			log.Printf("Assigning array at index %d with data %d from leftArray index %d with data %d", i, array[i], l, leftArray[l])
			array[i] = leftArray[l]
			l++
			i++
			log.Printf("Incrementing l to %d and i to %d", l, i)
		} else {
			log.Printf("rightArray index %d with data %d is less than leftArray index %d with data %d", r, rightArray[r], l, leftArray[l])
			log.Printf("Assigning array at index %d with data %d from rightArray index %d with data %d", i, array[i], r, rightArray[r])
			array[i] = rightArray[r]
			r++
			i++
			log.Printf("Incrementing r to %d and i to %d", r, i)
		}
	}
	log.Printf("Looping while l with data %d is less than the length of leftArray %d", l, leftArrLen)
	for l < leftArrLen {
		log.Printf("Assigning array at index %d with data %d from leftArray at index %d", i, leftArray[l], l)
		array[i] = leftArray[l]
		l++
		i++
		log.Printf("New index values: l = %d, i = %d", l, i)
	}
	log.Printf("Looping while r with data %d is less than the length of rightArray %d", r, rightArrLen)
	for r < rightArrLen {
		log.Printf("Assigning array at index %d with data %d from rightArray at index %d", i, rightArray[r], r)
		array[i] = rightArray[r]
		r++
		i++
		log.Printf("New index values: r = %d, i = %d", r, i)
	}
}

func main() {
	log.Println("Starting merge sort application")

	// Create 20 element array of random integers from 0-50
	var array []int
	for i := 0; i < 10; i++ {
		array = append(array, rand.Intn(50))
	}

	mergeSort(array, "main", 1)

	log.Println("Final array: ", array)

}
