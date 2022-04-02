def is_palindrome(word: str):
    word = word.lower()
    return word == word[::-1] 

while True:
    print(is_palindrome(input("Podaj wyraz: ")))
