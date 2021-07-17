package main

import (
	"fmt"
    "log"

    "github.com/pachyderm/pachyderm/src/client"
    "github.com/pachyderm/pachyderm/src/client/pfs"
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

    repos, err := c.ListRepo()
    if err != nil {
        log.Fatal(err)
    }
    fmt.Println(repos)
}

