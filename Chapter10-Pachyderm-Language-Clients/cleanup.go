package main

import (
	"fmt"
    "log"

    "github.com/pachyderm/pachyderm/src/client"
)

func main() {

	c, err := client.NewFromAddress("127.0.0.1:30650")
	if err != nil {
		log.Fatal(err)
	}

    if err := c.DeleteRepo("contour", true); err != nil {
		panic(err)
    }
    if err := c.DeleteRepo("photos", true); err != nil {
         panic(err)
    }
    if err := c.DeleteRepo("histogram", true); err != nil {
          panic(err)
    }
    if err := c.DeletePipeline("contour", true); err != nil {
          panic(err)
    }
    if err := c.DeletePipeline("histogram", true); err != nil {
          panic(err)
    }

    pipelines, err := c.ListPipeline()
    if err != nil {
        panic(err)
    }
    fmt.Println(pipelines)

    repos, err := c.ListRepo()
    if err != nil {
        log.Fatal(err)
    }
    fmt.Println(repos)
}
