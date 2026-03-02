import requests

BASE = "http://127.0.0.1:8000"

# Test 1: Negative ID 
bad_book = {"id": -1, "title": "Test", "author": "Me", "year": 2024}
r = requests.post(f"{BASE}/books", json=bad_book)
print("Negative ID:", r.status_code, r.json())
print("-"*50)

# Test 2: Empty title 
bad_book = {"id": 10, "title": "", "author": "Me", "year": 2024}
r = requests.post(f"{BASE}/books", json=bad_book)
print("Empty title:", r.status_code, r.json())
print("-"*50)
# Test 3: Invalid year 
bad_book = {"id": 10, "title": "Test", "author": "Me", "year": 3000}
r = requests.post(f"{BASE}/books", json=bad_book)
print("Year 3000:", r.status_code, r.json())
print("-"*50)
# Test 4: Valid book 
good_book = {"id": 10, "title": "Valid Book", "author": "Good Author", "year": 2024}
r = requests.post(f"{BASE}/books", json=good_book)
print("Valid book:", r.status_code, r.json())
print("-"*50)

print("=== TESTING SEARCH ===\n")

# Test 1: Search by author
print("1. Books by 'Orwell':")
r = requests.get(f"{BASE}/books/search?author=Orwell")
print(r.json())

# Test 2: Search by year
print("\n2. Books from 1960:")
r = requests.get(f"{BASE}/books/search?year=1960")
print(r.json())

# Test 3: Search by year range
print("\n3. Books from 1940-1970:")
r = requests.get(f"{BASE}/books/search?min_year=1940&max_year=1970")
print(r.json())

# Test 4: Combine filters
print("\n4. Books by 'Lee' from 1960:")
r = requests.get(f"{BASE}/books/search?author=Lee&year=1960")
print(r.json())

# Test 5: Old books (before 1950)
print("\n5. Books before 1950:")
r = requests.get(f"{BASE}/books/search?max_year=1950")
print(r.json())