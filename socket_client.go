package main

import (
	"fmt"
	"log"
	"net"
	"time"
)

func main() {
	conn, err := net.Dial("tcp", "baidu.com:80")
	if err != nil {
		log.Fatal(err)
	}
	req := []byte("POST / HTTP/1.0\n\n")
	res := make([]byte, 100)
	for {
		conn.Write(req)
		conn.Read(res)
		fmt.Println(string(res))
		time.Sleep(2 * time.Second)
	}
}
