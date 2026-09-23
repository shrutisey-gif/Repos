# Lists/Arrays and Manipulations

# Creating a starting list of cloud services
services = ["Lambda", "EC2", "App Service", "S3"]
print(f"Starting List: {services}")

# 1. Append: Adds an item to the end of the list
services.append("Blob Storage")
print(f"After Append: {services}")

# 2. Insert: Adds an item at a specific index position
services.insert(1, "Azure Functions")
print(f"After Insert at index 1: {services}")

# 3. Remove: Deletes the first occurrence of a specific value
services.remove("EC2")
print(f"After Remove 'EC2': {services}")

# 4. Pop: Removes and returns an item at a specific index (defaults to the last item)
popped_item = services.pop(3)
print(f"After Pop at index 3: {services}, Popped Item: {popped_item}")

# 5. Sort: Re-orders the list alphabetically or numerically
services.sort()
print(f"After Sort: {services}")

# 6. Slicing: Extracting a specific sub-section of the list [start:stop]
subset = services[0:2]
print(f"Slices items (index 0 and 1): {subset}")
