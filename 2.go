package main
import "fmt"

func summary(arr []int) int {
  var sum int = 0
  for i :=0; i<len(arr);i++ {
    sum += arr[i]
  }
  return sum
}

func multiply(arr []int) int {
  var sum int = 1
  for i :=0; i<len(arr); i++{
  sum *= arr[i]
}
  return sum
}



func main() {
  x := [] int{1,2,3,4,5,6,7,8}
fmt.Println(summary(x))
fmt.Println(multiply(x))
}
