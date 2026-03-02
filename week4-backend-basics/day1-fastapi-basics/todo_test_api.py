import requests

BASE = "http://127.0.0.1:8000"

print("TESTING ALL ERROR CODES\n")

# Test 1: Create valid todo (should be 201)
print("1. Create valid todo (expect 201):")
task = {"id": 10, "task": "New task", "completed": False}
r = requests.post(f"{BASE}/todos", json=task)
print(f"   Status: {r.status_code} {'✅' if r.status_code == 201 else '❌'}\n")

# Test 2: Create duplicate (should be 409)
print("2. Create duplicate ID (expect 409):")
r = requests.post(f"{BASE}/todos", json=task)
print(f"   Status: {r.status_code} {'✅' if r.status_code == 409 else '❌'}")
print(f"   Error: {r.json()}\n")

# Test 3: Update with ID mismatch (should be 400)
print("3. Update with ID mismatch (expect 400):")
wrong = {"id": 999, "task": "Wrong", "completed": True}
r = requests.put(f"{BASE}/todos/10", json=wrong)
print(f"   Status: {r.status_code} {'✅' if r.status_code == 400 else '❌'}")
print(f"   Error: {r.json()}\n")

# Test 4: Get non-existent (should be 404)
print("4. Get non-existent todo (expect 404):")
r = requests.get(f"{BASE}/todos/999")
print(f"   Status: {r.status_code} {'✅' if r.status_code == 404 else '❌'}\n")

# Test 5: Delete valid (should be 204)
print("5. Delete valid todo (expect 204):")
r = requests.delete(f"{BASE}/todos/10")
print(f"   Status: {r.status_code} {'✅' if r.status_code == 204 else '❌'}\n")

# Test 6: Invalid data (should be 422 - automatic!)
print("6. Invalid data - negative ID (expect 422):")
bad = {"id": -1, "task": "Bad", "completed": True}
r = requests.post(f"{BASE}/todos", json=bad)
print(f"   Status: {r.status_code} {'✅' if r.status_code == 422 else '❌'}\n")

print("🎉 All error codes tested!")