package main

 import (
     "fmt"
     "log"
     "github.com/gogo/protobuf/types"
     "github.com/pachyderm/pachyderm/v2/src/client"
)

func main() {
     c, err := client.NewFromURI("grpc://localhost:30650")
     if err != nil {
         log.Fatal(err)
     }

     version, err := c.VersionAPIClient.GetVersion(c.Ctx(), &types.Empty{})
     if err != nil {
         panic(err)
     }
     fmt.Println(version)
}

