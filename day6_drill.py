with open("Saifullah.txt" ,"w") as file :
    file.write("Great Saif")
    
with open("Saifullah.txt" ,"r") as file :
    print(file.read())
print("=========================================================================")

import json

history = [{"role" : "user" , "text" : "happy"}]

with open("history.json" , "w") as f:
    json.dump(history,f)
    
# Load
with open("history.json", "r") as f:
    loaded_history = json.load(f)
    print(loaded_history)  # Output: [{'role': 'user', 'text': 'happy'}]
    
print("=========================================================================")
import json

# 1. Create a Python object
my_data = {
    "user": "Suleman",
    "scores": [95, 87, 92],
    "is_active": True
}

# 2. SAVE: Python → JSON → File
with open("test.json", "w") as f:
    json.dump(my_data, f, indent=5)
print("✅ Saved to test.json")

# 3. LOAD: File → JSON → Python
with open("test.json", "r") as f:
    loaded_data = json.load(f)
print("✅ Loaded from test.json")
print(loaded_data)

# 4. Verify it's the same
print(my_data == loaded_data)  # Should print True