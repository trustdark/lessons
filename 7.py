def diagonalReverse(list):
        for x in range(len(list[0])):
            for y in range(len(list)):
                print(list[y][x], end="")
                y=y+1
            print("")
            x=x+1


arr = [[1,2,3],
       [4,5,6],
       [7,8,9]]


diagonalReverse(arr)
