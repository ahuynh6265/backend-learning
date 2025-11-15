#string functions with pytest

def capitalize_word(text):
  return ' '.join(word.capitalize() for word in text.split())

def reverse_word(text):
  return text[::-1]

def count_vowels(text):
  vowels ="aeiouAEIOU"
  return sum(1 for char in text if char in vowels)

def is_palindrome(text):
  palindrome =''.join(text.lower().split())
  return palindrome == palindrome[::-1]

def main():
  word = input(("Enter a word: "))
  print(capitalize_word(word))
  print(reverse_word(word))
  print(count_vowels(word))
  print(is_palindrome(word))

if __name__ == "__main__":
  main()