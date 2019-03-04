def caesarCipher(str, key):
    new_list = []
    for index, value in enumerate(str):
        new_num = ord(value) + key
        if ord(value) == 32:
            new_list = new_list + [" "]
        elif 96 < ord(value) < 123:
            if new_num < 122:
                new_list = new_list + [chr(new_num)]
            else:
                new_list = new_list + [chr(new_num-26)]
        elif 64 < ord(value) < 91:
            if new_num < 90:
                new_list = new_list + [chr(new_num)]
            else:
                new_list = new_list + [chr(new_num-26)]
        else:
            print("Restricted symbols detected. String below encrypted incorrectly.")
    print(''.join(new_list))

text = "python.   x"
caesarCipher(text, 14)


# def caesarCipher(str, key):
#     new_string = ""
#     for index, value in enumerate(str):
#         if ord(value) == 32:
#             print(" ")
#         elif 96 < ord(value) < 123:
#             new_num = ord(value) + key
#             if ord(value) + key < 122:
#                 new_string = new_string + str([chr(new_num)])
#             else:
#                 new_string = new_string + str([chr(new_num-26)])
#     print(new_string)

# for index, value in enumerate(text):
#     print(ord(value))
# print(chr(97))

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
