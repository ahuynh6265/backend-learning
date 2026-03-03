import requests

BASE = "http://127.0.0.1:8000"

print("test initial vals")
#negative value
product = {"id": -1, "name": "Keyboard", "price": 79.99, "stock": 40}
r = requests.post(f"{BASE}/products", json=product)
print(r.status_code, r.json())
print("-"*50)

#no name value
product = {"id": 5, "name": "", "price": 79.99, "stock": 40}
r = requests.post(f"{BASE}/products", json=product)
print(r.status_code, r.json())
print("-"*50)

#negative price value
product = {"id": 5, "name": "Keyboard", "price": -100.23, "stock": 40}
r = requests.post(f"{BASE}/products", json=product)
print(r.status_code, r.json())
print("-"*50)

#negative stock value
product = {"id": 5, "name": "Keyboard", "price": 79.99, "stock": -29}
r = requests.post(f"{BASE}/products", json=product)
print(r.status_code, r.json())
print("-"*50)


print("=== Testing post(create) ===")
#duplicate id create
product = {"id": 3, "name": "Keyboard", "price": 79.99, "stock": 40}
r = requests.post(f"{BASE}/products", json=product)
print(r.status_code, r.json())
print("-"*50)

#good create
product = {"id": 5, "name": "Keyboard", "price": 79.99, "stock": 40}
r = requests.post(f"{BASE}/products", json=product)
print(r.status_code, r.json())
print("-"*50)

# test search
print("1. Search price above 500:")
r = requests.get(f"{BASE}/products/search?min_price=500.00")
print(r.json())
print()

print("2. Search laptop:")
r = requests.get(f"{BASE}/products/search?name=laptop")
print(r.json())


print("=== Testing delete ===")
#valid delete
r = requests.delete(f"{BASE}/products/1")
print(r.status_code)
print("-"*50)

#invalid delete 
r = requests.delete(f"{BASE}/products/100")
print(r.status_code)
print("-"*50)

print("=== Testing update ===")
#valid update 
product = {"id": 2, "name": "Headphones", "price": 49.99, "stock": 8}
r = requests.put(f"{BASE}/products/2", json=product)
print(r.status_code, r.json())
print("-"*50)

#id mismatch 
product = {"id": 5, "name": "Headphones", "price": 49.99, "stock": 8}
r = requests.put(f"{BASE}/products/2", json=product)
print(r.status_code, r.json())
print("-"*50)

#no id found
product = {"id": 100, "name": "Headphones", "price": 49.99, "stock": 8}
r = requests.put(f"{BASE}/products/100", json=product)
print(r.status_code, r.json())
print("-"*50)