# Dictionaries Creation and Manipulations

# 1. Creation: Defining a dictionary representing a virtual server config
server_config = {
    "provider": "AWS",
    "instance_type": "t3.micro",
    "os": "Ubuntu 22.04",
    "storage_gb": 30
}
print(f"Initial Dictionary: {server_config}")

# 2. Accessing a value using its key
print(f"Accessing 'provider': {server_config['provider']}")

# 3. Manipulation (Update): Changing an existing value
server_config["storage_gb"] = 50
print(f"After Update 'storage_gb': {server_config}")

# 4. Manipulation (Add): Creating a brand new key-value pair
server_config["environment"] = "Development"
print(f"After Add 'environment': {server_config}")

# 5. Deleting a key-value pair
del server_config["os"]
print(f"After Deleting 'os': {server_config}")

# 6. Safe Read (Get Method): Prevents program from crashing if a key doesn't exist
# Returns a fallback default value instead of a KeyError
key = server_config.get("key_code", "No key code Provided")
print(f"'key_code': {key}")

# 7. Safe Read (Get Method) with User Input
# Ask the user to type a key (e.g., type 'provider', 'instance_type', or a fake key like 'billing_code')
user_input = input("Enter the configuration setting you want to check: ")

# The .get() method looks for whatever the user typed. 
# If it doesn't exist, it falls back to the default message.
search_result = server_config.get(user_input, "Key not provided / does not exist")

print(f"Result for '{user_input}': {search_result}")
