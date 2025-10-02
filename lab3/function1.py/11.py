def get_palindrom(word):
    if word==word[::-1]:
       print("Yes, it is a palindrom")
    else:
        print("No, it is not a palindrom" )
word=input()
get_palindrom(word) 