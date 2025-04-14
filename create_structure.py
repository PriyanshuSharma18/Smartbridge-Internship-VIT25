import os

names = ["Ankur Jha", "Priyanshu Sharma", "Farha Ansari", "Ryan Santosh Joseph"]

for name in names:
    for i in range(1, 5):
        path = os.path.join(name, f"Assignment {i}")
        os.makedirs(path, exist_ok=True)
        with open(os.path.join(path, ".gitkeep"), "w") as f:
            pass

print("✅ All folders created.")
