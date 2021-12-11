package main

 import (
     "fmt"
     "log"
     "os"

     "github.com/pachyderm/pachyderm/v2/src/client"
     "github.com/pachyderm/pachyderm/v2/src/pfs"
     "github.com/pachyderm/pachyderm/v2/src/pps"
 )

 func main() {

     c, err := client.NewOnUserMachine("kilgore@kilgore.trout")
     if err != nil {
         log.Fatal(err)
     }


     if _, err := c.PfsAPIClient.CreateRepo(
         c.Ctx(),
         &pfs.CreateRepoRequest{
             Repo:        client.NewRepo("photos"),
             Description: "A repository that stores images.",
             Update:      true,
         },
     ); err != nil {
        panic(err)
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

     files, err := c.ListFileAll(myCommit, "/")
     if err != nil {
         panic(err)
     }

     fmt.Println(files)
 

     repos, err := c.ListRepo()
     if err != nil {
         log.Fatal(err)
     }
     fmt.Println(repos)
}
