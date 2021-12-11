package main

 import (
     "log"
     "fmt"
     "os"

     "github.com/pachyderm/pachyderm/v2/src/client"
)

func main() {

     c, err := client.NewOnUserMachine("user")
     if err != nil {
         log.Fatal(err)
     }

     myCommit := client.NewCommit("photos","master", "")

     f1, err := os.Open("landscape.png")
     if err != nil {
         panic(err)
     }

     if err := c.PutFile(myCommit, "landscape.png", f1); err != nil {
         panic(err)
     }

     f2, err := os.Open("brown_vase.png")
     if err != nil {
         panic(err)
     }

     if err := c.PutFile(myCommit, "brown_vase.png", f2); err != nil {
         panic(err)
     }

     f3, err := os.Open("hand.png")
     if err != nil {
         panic(err)
     }

     if err := c.PutFile(myCommit, "hand.png", f3); err != nil {
         panic(err)
     }

     files, err := c.ListFileAll(myCommit, "/")
     if err != nil {
         panic(err)
     }

     fmt.Println(files)
}
