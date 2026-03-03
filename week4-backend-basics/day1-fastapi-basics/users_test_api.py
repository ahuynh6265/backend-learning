import requests

BASE = "http://127.0.0.1:8000"

print("test initial vals")
#negative value
user = {"id": -1, "name": "Dwyane Wade", "email": "dwade@email.com", "age": 42}
r = requests.post(f"{BASE}/users", json=user)
print(r.status_code, r.json())
print("-"*50)

#no name value
user = {"id": 6, "name": "", "email": "dwade@email.com", "age": 42}
r = requests.post(f"{BASE}/users", json=user)
print(r.status_code, r.json())
print("-"*50)

#no specie value
user = {"id": 6, "name": "Dwyane Wade", "email": "", "age": 42}
r = requests.post(f"{BASE}/users", json=user)
print(r.status_code, r.json())
print("-"*50)

#invalid age value
user = {"id": 6, "name": "Dwyane Wade", "email": "dwade@email.com", "age": 12}
r = requests.post(f"{BASE}/users", json=user)
print(r.status_code, r.json())
print("-"*50)




print("=== Testing post(create) ===")
#duplicate id create
user = {"id": 1, "name": "Dwyane Wade", "email": "dwade@email.com", "age": 42}
r = requests.post(f"{BASE}/users", json=user)
print(r.status_code, r.json())
print("-"*50)

#good create
user = {"id": 7, "name": "Dwyane Wade", "email": "dwade@email.com", "age": 42}
r = requests.post(f"{BASE}/users", json=user)
print(r.status_code, r.json())
print("-"*50)

print("=== Testing delete ===")
#valid delete
r = requests.delete(f"{BASE}/users/1")
print(r.status_code)
print("-"*50)

#invalid delete 
r = requests.delete(f"{BASE}/users/100")
print(r.status_code)
print("-"*50)

print("=== TESTING SEARCH ===\n")

# Test filters combining correctly
print("1. Search 'Dwyane' age 42+:")
r = requests.get(f"{BASE}/users/search?name=Dwyane&min_age=42")
print(r.json())
print()

print("2. Age 32:")
r = requests.get(f"{BASE}/users/search?min_age=32&max_age=32")
print(r.json())

print("=== Testing update ===")
#valid update 
user = {"id": 2, "name": "Michael Jordan", "email": "mjordan@email.com", "age": 49}
r = requests.put(f"{BASE}/users/2", json=user)
print(r.status_code, r.json())
print("-"*50)

#id mismatch 
user = {"id": 5, "name": "Michael Jordan", "email": "mjordan@email.com", "age": 49}
r = requests.put(f"{BASE}/users/2", json=user)
print(r.status_code, r.json())
print("-"*50)

#no id found
user = {"id": 100, "name": "Michael Jordan", "email": "mjordan@email.com", "age": 49}
r = requests.put(f"{BASE}/users/100", json=user)
print(r.status_code, r.json())
print("-"*50)