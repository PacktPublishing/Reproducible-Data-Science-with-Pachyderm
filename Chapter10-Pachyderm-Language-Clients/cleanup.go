package main

 import (
     "log"
     "fmt"

     "github.com/pachyderm/pachyderm/v2/src/client"
)

func main() {

     c, err := client.NewOnUserMachine("user")
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

     pipelines, err := c.ListPipeline(true)
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

