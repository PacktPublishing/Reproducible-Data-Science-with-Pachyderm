package main

import (
	"fmt"
    "log"

    "github.com/gogo/protobuf/types"
    "github.com/pachyderm/pachyderm/src/client"
)

func main() {

	c, err := client.NewFromAddress("127.0.0.1:30650")
	if err != nil {
		log.Fatal(err)
	}

    version, err := c.VersionAPIClient.GetVersion(c.Ctx(), &types.Empty{})
    if err != nil {
		panic(err)
	}
	fmt.Println(version)
}
