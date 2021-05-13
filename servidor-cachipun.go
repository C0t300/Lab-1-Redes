package main

import (
	"fmt"
	"math/rand"
	"net"
	"strconv"
	"strings"
	"time"
)

func randomInt(max int, min int) int {
	rand.Seed(time.Now().UnixNano())
	return rand.Intn(max-min) + min // range is min to max
}

func true80Percent() bool {
	a := randomInt(11, 1)
	if a <= 8 {
		fmt.Println("true80 TRUE")
		return true
	}
	fmt.Println("true80 FALSE")
	return false
}

func cachipun() string {
	var r int = randomInt(4, 1)
	if r == 1 {
		return "tijera"
	} else if r == 2 {
		return "papel"
	} else if r == 3 {
		return "piedra"
	} else {
		fmt.Println("uh oh")
		return "false"
	}
}

func main() {

	PUERTO := ":50102"
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

	fmt.Println("Cachipun escuchando en ", PUERTO)

	buf := make([]byte, BUF)

	n, addr, err := con.ReadFromUDP(buf)

	fmt.Println("Recibido mensaje ", string(buf))

	if strings.TrimSpace(string(buf[0:n])) == "game" {
		fmt.Println("inside if")
		if true80Percent() {
			NEWPORT := strconv.Itoa(randomInt(50200, 50100))
			fmt.Println("Nuevo puerto ", NEWPORT)
			msg := []byte("OK|" + NEWPORT)
			NEWPORT = ":" + NEWPORT
			_, err = con.WriteToUDP(msg, addr)
			fmt.Println("Mensaje enviado ", string(buf))
			con.Close()
			s, _ := net.ResolveUDPAddr("udp4", NEWPORT)
			con, _ := net.ListenUDP("udp4", s)
			n, addr, _ := con.ReadFromUDP(buf)
			flag := strings.TrimSpace(string(buf[0:n])) != "close"
			for flag {
				if strings.TrimSpace(string(buf[0:n])) == "play" {
					msg := []byte(cachipun())
					_, err = con.WriteToUDP(msg, addr)
				}
				n, addr, _ = con.ReadFromUDP(buf)
				flag = strings.TrimSpace(string(buf[0:n])) != "close"
			}

		} else {
			msg := []byte("NO")
			fmt.Println("No disponible")
			_, err = con.WriteToUDP(msg, addr)
		}
		return
	}
}
