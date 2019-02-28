def isPalindrome(str):
    original = str[::-1]
    if original==str:
        print("Palindrome here:", str)
    else:
        print("No palindrome in this string ", str)

string = "radar"
isPalindrome(string)
