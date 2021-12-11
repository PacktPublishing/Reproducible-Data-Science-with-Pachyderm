package main

 import (
     "fmt"
     "log"

     "github.com/pachyderm/pachyderm/v2/src/client"
     "github.com/pachyderm/pachyderm/v2/src/pfs"

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

     repos, err := c.ListRepo()
     if err != nil {
         log.Fatal(err)
     }
     fmt.Println(repos)
 }

