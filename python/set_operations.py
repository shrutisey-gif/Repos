# Set Operations on Lists

# Two lists containing overlapping deployment tools (with duplicates in list_a)
list_a = ["Docker", "Terraform", "Docker", "Ansible", "Kubernetes"]
list_b = ["Terraform", "Jenkins", "Kubernetes", "GitLab CI"]

print(f"List A (with duplicates): {list_a}")
print(f"List B: {list_b}")
print(f"list_a + list_b: {list_a + list_b}")

# 1. Type Casting to Set: Instantly strips out duplicate values
set_a = set(list_a)
set_b = set(list_b)
print(f"Set A (unique): {set_a}")

# 2. Intersection: Finds items that exist in BOTH collections
common = set_a.intersection(set_b)
print(f"Common in both sets: {common}")

# 3. Union: Merges both collections together completely, leaving no duplicates
union = set_a.union(set_b)
print(f"Union of both sets: {union}")

# 4. Difference: Finds items in Set A that do NOT exist in Set B
difference = set_a.difference(set_b)
print(f"Items in A but not in B: {difference}")
