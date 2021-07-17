package main

import (
	"fmt"
    "log"
    "os"

    "github.com/pachyderm/pachyderm/src/client"
)

func main() {

	c, err := client.NewFromAddress("127.0.0.1:30650")
	if err != nil {
		log.Fatal(err)
	}

    f, err := os.Open("red_vase.png")
	if err != nil {
		panic(err)
	}
    if _, err := c.PutFile("photos", "master", "red_vase.png", f); err != nil {
		panic(err)
	}

    f2, err := os.Open("landscape.png")
    if err != nil {
        panic(err)
    }
    if _, err := c.PutFile("photos", "master", "landscape.png", f2); err != nil {
        panic(err)
    }

    f3, err := os.Open("hand.png")
    if err != nil {
        panic(err)
    }
    if _, err := c.PutFile("photos", "master", "hand.png", f3); err != nil {
        panic(err)
    }

    files, err := c.ListFile("photos", "master", "/")
    if err != nil {
        panic(err)
    }
    fmt.Println(files)
}

