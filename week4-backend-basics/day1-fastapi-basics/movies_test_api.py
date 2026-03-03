import requests

BASE = "http://127.0.0.1:8000"

print("test initial vals")
#negative value
movie = {"id": -1, "title": "Sinners", "director": "Ryan Coogler", "year": 2025, "rating": 9.4}
r = requests.post(f"{BASE}/movies", json=movie)
print(r.status_code, r.json())
print("-"*50)

#no title value
movie = {"id": 5, "title": "", "director": "Ryan Coogler", "year": 2025, "rating": 9.4}
r = requests.post(f"{BASE}/movies", json=movie)
print(r.status_code, r.json())
print("-"*50)

#no director value
movie = {"id": 5, "title": "Sinners", "director": "", "year": 2025, "rating": 9.4}
r = requests.post(f"{BASE}/movies", json=movie)
print(r.status_code, r.json())
print("-"*50)

#invalid year value
movie = {"id": 5, "title": "Sinners", "director": "Ryan Coogler", "year": 1899, "rating": 9.4}
r = requests.post(f"{BASE}/movies", json=movie)
print(r.status_code, r.json())
print("-"*50)

#invalid rating value
movie = {"id": 5, "title": "Sinners", "director": "Ryan Coogler", "year": 1899, "rating": 10.1}
r = requests.post(f"{BASE}/movies", json=movie)
print(r.status_code, r.json())
print("-"*50)


print("=== Testing post(create) ===")
#duplicate id create
movie = {"id": 3, "title": "Sinners", "director": "Ryan Coogler", "year": 2025, "rating": 9.4}
r = requests.post(f"{BASE}/movies", json=movie)
print(r.status_code, r.json())
print("-"*50)

#good create
movie = {"id": 5, "title": "Sinners", "director": "Ryan Coogler", "year": 2025, "rating": 9.4}
r = requests.post(f"{BASE}/movies", json=movie)
print(r.status_code, r.json())
print("-"*50)

print("=== Testing update ===")
#valid update 
movie = {"id": 3, "title": "Hacksaw Ridge", "director": "Andrew Garfield", "year": 2003, "rating": 7.4}
r = requests.put(f"{BASE}/movies/3", json=movie)
print(r.status_code, r.json())
print("-"*50)

#id mismatch 
movie = {"id": 5, "title": "Hacksaw Ridge", "director": "RAndrew Garfield", "year": 2003, "rating": 7.4}
r = requests.put(f"{BASE}/movies/2", json=movie)
print(r.status_code, r.json())
print("-"*50)

#no id found
movie = {"id": 100, "title": "Hacksaw Ridge", "director": "Andrew Garfield", "year": 2003, "rating": 7.4}
r = requests.put(f"{BASE}/movies/100", json=movie)
print(r.status_code, r.json())
print("-"*50)

print("=== Testing delete ===")
#valid delete
r = requests.delete(f"{BASE}/movies/1")
print(r.status_code)
print("-"*50)

#invalid delete 
r = requests.delete(f"{BASE}/movies/100")
print(r.status_code)
print("-"*50)