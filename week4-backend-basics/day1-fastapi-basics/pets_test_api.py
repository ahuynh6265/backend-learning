import requests

BASE = "http://127.0.0.1:8000"

print("test initial vals")
#negative value
pet = {"id": -1, "name": "Lucky", "species": "dog", "age": 7}
r = requests.post(f"{BASE}/pets", json=pet)
print(r.status_code, r.json())
print("-"*50)

#no name value
pet = {"id": 5, "name": "", "species": "dog", "age": 7}
r = requests.post(f"{BASE}/pets", json=pet)
print(r.status_code, r.json())
print("-"*50)

#no specie value
pet = {"id": 5, "name": "Lucky", "": "dog", "age": 7}
r = requests.post(f"{BASE}/pets", json=pet)
print(r.status_code, r.json())
print("-"*50)

#negative age value
pet = {"id": 5, "name": "Lucky", "species": "dog", "age": -1}
r = requests.post(f"{BASE}/pets", json=pet)
print(r.status_code, r.json())
print("-"*50)




print("=== Testing post(create) ===")
#duplicate id create
pet = {"id": 1, "name": "Lucky", "species": "dog", "age": 7}
r = requests.post(f"{BASE}/pets", json=pet)
print(r.status_code, r.json())
print("-"*50)

#good create
pet = {"id": 4, "name": "Simba", "species": "lion", "age": 14}
r = requests.post(f"{BASE}/pets", json=pet)
print(r.status_code, r.json())
print("-"*50)

print("=== Testing delete ===")
#valid delete
r = requests.delete(f"{BASE}/pets/1")
print(r.status_code)
print("-"*50)

#invalid delete 
r = requests.delete(f"{BASE}/pets/100")
print(r.status_code)
print("-"*50)

print("=== Testing update ===")
#valid update 
pet = {"id": 2, "name": "Tom", "species": "tiger", "age": 9}
r = requests.put(f"{BASE}/pets/2", json=pet)
print(r.status_code, r.json())
print("-"*50)

#id mismatch 
pet = {"id": 5, "name": "Tom", "species": "tiger", "age": 9}  
r = requests.put(f"{BASE}/pets/2", json=pet)
print(r.status_code, r.json())
print("-"*50)

#no id found
pet = {"id": 100, "name": "Tom", "species": "tiger", "age": 9}  
r = requests.put(f"{BASE}/pets/100", json=pet)
print(r.status_code, r.json())
print("-"*50)