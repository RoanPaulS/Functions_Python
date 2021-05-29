word = input("Enter any word : ");

def palindrome(word):
    return word == word[::-1];


if palindrome(word):
    print("Given word is Palindrome");

else:
    print("Given word is not a Palindrome");
