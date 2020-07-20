package main

import (
	"fmt"
	"sync"
)

const max = 100

func main() {
	n := 1
	c1 := make(chan int)
	c2 := make(chan int)
	wg := sync.WaitGroup{}
	wg.Add(1)
	go func() {
		fmt.Println(n)
		c2 <- n + 1
		for {
			select {
			case v := <-c1:
				if v > max {
					wg.Done()
					return
				}
				fmt.Println(v)
				c2 <- v + 1
			}
		}
	}()
	go func() {
		for {
			select {
			case v := <-c2:
				if v > max {
					wg.Done()
					return
				}
				fmt.Println(v)
				c1 <- v + 1
			}
		}
	}()
	wg.Wait()
}
