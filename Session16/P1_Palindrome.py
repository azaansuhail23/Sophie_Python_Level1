#Step 1: 
word=input("Enter a word that you want to check is palindrome ")

#Step 2: 
reverse=word[::-1]

#Step3 : Check Palindrome
if word==reverse:
    print("Palindrome")
else:
    print("Not a palindrome")
