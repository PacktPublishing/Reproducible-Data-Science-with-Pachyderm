package main

import (
	"fmt"
    "log"

    "github.com/pachyderm/pachyderm/src/client"
    "github.com/pachyderm/pachyderm/src/client/pps"
)

func main() {

	c, err := client.NewFromAddress("127.0.0.1:30650")
	if err != nil {
		log.Fatal(err)
	}

    if err := c.CreatePipeline(
        "contour",
        "svekars/contour-histogram:0.85",
        []string{"python3", "/contour.py"},
        []string{},
        &pps.ParallelismSpec{
            Constant: 1,
        },
        client.NewPFSInput("photos", "/"),
        "",
        false,
    ); err != nil {
        panic(err)
    }

    if err := c.CreatePipeline(
        "histogram",
        "svekars/contour-histogram:0.85",
        []string{"python3", "/histogram.py"},
        []string{},
        &pps.ParallelismSpec{
            Constant: 1,
        },
        client.NewPFSInput("contour", "/"),
        "",
        false,
    ); err != nil {
        panic(err)
    }

    pipelines, err := c.ListPipeline()
    if err != nil {
        panic(err)
    }
    fmt.Println(pipelines)
}
