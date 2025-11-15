from stringfunctions import capitalize_word, reverse_word, count_vowels, is_palindrome

def test_capitalize_words():
    assert capitalize_word("hello world") == "Hello World"
    assert capitalize_word("HELLO WORLD") == "Hello World"
    assert capitalize_word("hello") == "Hello"
    assert capitalize_word("") == ""

def test_reverse_string():
    assert reverse_word("hello") == "olleh"
    assert reverse_word("abc") == "cba"
    assert reverse_word("") == ""
    assert reverse_word("a") == "a"

def test_count_vowels():
    assert count_vowels("hello") == 2
    assert count_vowels("aeiou") == 5
    assert count_vowels("xyz") == 0
    assert count_vowels("") == 0

def test_is_palindrome():
    assert is_palindrome("racecar") == True
    assert is_palindrome("hello") == False
    assert is_palindrome("A man a plan a canal Panama") == True
    assert is_palindrome("") == True