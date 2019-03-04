def charFreq(str):
    arr_for_comp = []
    for i in range(97, 123):
        arr_for_comp = arr_for_comp + [chr(i)]
    for index, value in enumerate(arr_for_comp):
        print("{0} is present for {1} times".format(value, str.count(value)))







string = "abbabcbdbadcdcdcdfjkjaljfgzzzXXXX"

charFreq(string)
