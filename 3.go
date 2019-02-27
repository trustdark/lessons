package main
import "fmt"

func reverse(s string) {
  var ns string
for i :=0; i<len(s);i++ {
  ns += s[len(s)-i]
}
  fmt.Println()
}



func main() {
reverse("I am testing")
}
