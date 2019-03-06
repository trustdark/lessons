def brack_eval(str):
    int = 0
    for i, value in enumerate(str):
        if value == "[":
            int += 1
        elif value == "]":
            if int > 0:
                int -= 1
            else:
                continue
        else:
            return print("String incorrect")
    if int == 0:
        print("Brackets are fine")
    else:
        print("NOT OK")




x = "[]p"
brack_eval(x)
