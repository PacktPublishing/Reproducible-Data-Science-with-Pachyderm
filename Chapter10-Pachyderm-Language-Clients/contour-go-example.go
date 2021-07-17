package main

 import (
     "fmt"
     "log"
     "os"

     "github.com/pachyderm/pachyderm/src/client"
     "github.com/pachyderm/pachyderm/src/client/pfs"
     "github.com/pachyderm/pachyderm/src/client/pps"
 )

 func main() {

     c, err := client.NewFromAddress("127.0.0.1:30650")
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

     files, err := c.ListFile("photos", "master", "/")
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
