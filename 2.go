package main
import "fmt"

func sum(arr [8]int) int {
  var sum int = 0
  for i :=0; i<len(arr);i++ {
    sum += arr[i]
  }
  return sum
}

func main() {
  x := [8] int{1,2,3,4,5,6,7,8}
  fmt.Println(sum(x))
}
