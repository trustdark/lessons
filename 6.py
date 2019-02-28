def caesarCipher(str, key):
    new_list = []
    for index, value in enumerate(str):
        if value == 32:
            print(" ")
        elif 96 < ord(value) < 123:
            new_num = ord(value) + key
            if ord(value) + key < 122:
                new_list =new_list + [chr(new_num)]
            else:
                new_list =new_list + [chr(new_num-26)]
    for index, value in enumerate(new_list):
        print(value, end="")
    print()




text = "python"
# for index, value in enumerate(text):
#     print(ord(value))
# print(chr(97))

caesarCipher(text, 14)



# 65-90 uppercase
# 97-122 lowercase


# def caesarCipher(str, key):
#     #new_string = ""
#     for index, value in enumerate(str):
#         if value == 32:
#             print(" ")
#         elif 96 < ord(value) < 123:
#             new_num = ord(value) + key
#             if ord(value) + key < 122:
#                 print(chr(new_num), end='')
#             else:
#                 print(chr(new_num - 26), end='')
