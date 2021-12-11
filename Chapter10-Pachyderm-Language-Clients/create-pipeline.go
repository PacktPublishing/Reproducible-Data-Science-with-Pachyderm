package main

 import (
     "log"
     "fmt"

     "github.com/pachyderm/pachyderm/v2/src/client"
     "github.com/pachyderm/pachyderm/v2/src/pps"
)

func main() {

     c, err := client.NewOnUserMachine("user")
     if err != nil {
         log.Fatal(err)
     }

     if err := c.CreatePipeline(
         "contour",
         "svekars/contour-histogram:1.0 ",
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
         "svekars/contour-histogram:1.0",
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

     pipelines, err := c.ListPipeline(true)
     if err != nil {
         panic(err)
     }
     fmt.Println(pipelines)
 }

