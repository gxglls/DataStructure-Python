package main

import "fmt"

func main() {
	res := []int{3, 21, 4, 131, 23, 4, 4, 12, 1, 34, 2, 674, 89, 1, 25, 15, 3512}
	//res := []int{3, 1, 4, 2}
	sort(&res, 0, len(res)-1)
	fmt.Println(res)
}

//3,1,4,2
func sort(nums *[]int, left int, right int) {
	if left > right {
		return
	}
	mid := left
	oldRight := right
	for left < right {
		for (*nums)[left] <= (*nums)[mid] && left <= right{
			left++
		}
		for (*nums)[right] >= (*nums)[mid] && left <= right{
			right--
		}
		if right < left {
			break
		}
		(*nums)[right], (*nums)[left] = (*nums)[left], (*nums)[right]

	}
	(*nums)[mid], (*nums)[right] = (*nums)[right], (*nums)[mid]
	sort(nums, mid, right-1)
	sort(nums, right+1, oldRight)
}
