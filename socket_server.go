package main

import (
	"fmt"
	"log"
	"net"
)

func main() {
	l, err := net.Listen("tcp", "10.130.200.128:1111")
	if err != nil {
		log.Fatal(err)
	}
	for {
		conn, err := l.Accept()
		if err != nil {
			log.Fatal(err)
		}
		go handler(conn)
	}
}

func handler(conn net.Conn) {
	buffer := make([]byte, 2)
	for {
		conn.Read(buffer)
		fmt.Println(buffer)
	}
}
