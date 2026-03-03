import requests

BASE = "http://127.0.0.1:8000"

print("test initial vals")
#negative value
note = {"id": -1, "title": "Recipie for chicken alfredo", "content": "cook chicken, boil noodles, make sauce, add all together"}
r = requests.post(f"{BASE}/notes", json=note)
print(r.status_code, r.json())
print("-"*50)

#no title value
note = {"id": 5, "title": "", "content": "cook chicken, boil noodles, make sauce, add all together"}
r = requests.post(f"{BASE}/notes", json=note)
print(r.status_code, r.json())
print("-"*50)

#negative content value
note = {"id": 5, "title": "Recipie for chicken alfredo", "content": -100.23}
r = requests.post(f"{BASE}/notes", json=note)
print(r.status_code, r.json())
print("-"*50)


print("=== Testing post(create) ===")
#duplicate id create
note = {"id": 3, "title": "Recipie for chicken alfredo", "content": "cook chicken, boil noodles, make sauce, add all together"}
r = requests.post(f"{BASE}/notes", json=note)
print(r.status_code, r.json())
print("-"*50)

#good create
note = {"id": 5, "title": "Recipie for chicken alfredo", "content": "cook chicken, boil noodles, make sauce, add all together"}
r = requests.post(f"{BASE}/notes", json=note)
print(r.status_code, r.json())
print("-"*50)

print("=== Testing delete ===")
#valid delete
r = requests.delete(f"{BASE}/notes/1")
print(r.status_code)
print("-"*50)

#invalid delete 
r = requests.delete(f"{BASE}/notes/100")
print(r.status_code)
print("-"*50)

print("=== Testing update ===")
#valid update 
note = {"id": 2, "title": "Best Buy item list", "content": "keyboard, computer, monitor, headphones, and mouse"}
r = requests.put(f"{BASE}/notes/2", json=note)
print(r.status_code, r.json())
print("-"*50)

#id mismatch 
note = {"id": 5, "title": "Best Buy item list", "content": "keyboard, computer, monitor, headphones, and mouse"}
r = requests.put(f"{BASE}/notes/2", json=note)
print(r.status_code, r.json())
print("-"*50)

#no id found
note = {"id": 100, "title": "Best Buy item list", "content": "keyboard, computer, monitor, headphones, and mouse"}
r = requests.put(f"{BASE}/notes/100", json=note)
print(r.status_code, r.json())
print("-"*50)