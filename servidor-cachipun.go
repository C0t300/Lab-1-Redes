package main

import (
	"fmt"
	"net"
	"strings"
)

func main() {

	PUERTO := ":50100"
	BUF := 1024

	s, err := net.ResolveUDPAddr("udp4", PUERTO)
	if err != nil {
		fmt.Println(err)
		return
	}

	con, err := net.ListenUDP("udp4", s)
	if err != nil {
		fmt.Println(err)
		return
	}

	defer con.Close()
	buf := make([]byte, BUF)

	for {
		n, addr, err := con.ReadFromUDP(buf)
		fmt.Println(string(buf[0 : n-1]))

		if strings.TrimSpace(string(buf[0:n])) == "STOP" {
			fmt.Println("Saliendo del Servidor")
			return
		}

		msg := []byte("Hola de welta")
		fmt.Println("Exit: ", string(msg))
		_, err = con.WriteToUDP(msg, addr)
		if err != nil {
			fmt.Println(err)
			return
		}
	}
}
