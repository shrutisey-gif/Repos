# OS Library and 5 Commands
import os

# 1. Get Current Working Directory (getcwd)
current_dir = os.getcwd()
print(f"Current Directory: {current_dir}")
# OR
print(f"Current Working Directory: {os.getcwd()}")

# 2. List Folders (listdir)
Directory = os.listdir(current_dir)
print(f"Directory Contents: {Directory}")
# OR
print(f"Files and Folders in Current Directory: {os.listdir(os.getcwd())}")

# Displays everything inside your current working folder
_ , directories , files = next(os.walk(current_dir))
print("📁 Directories found:", directories)
print("📄 Files found:", files)

# 3. Create a New Directory (mkdir)
# Creates a temporary folder inside your project directory if it doesn't exist yet
new_folder = "logs"
if not os.path.exists(new_folder):
    os.mkdir(new_folder)
    print(f"Created new folder: '{new_folder}'")
else:
    print(f"Folder '{new_folder}' already exists.")

# 4. Check Environment Variables (environ.get)
# Checks the system name of your computer's OS profile
user_profile = os.environ.get("USERNAME")
print(f"User Profile: {user_profile}")

# 5. Path Join (path.join)
# Dynamically connects file paths safely based on your OS rules (slashes vs backslashes)
secure_file_path = os.path.join(current_dir, new_folder, "app.log")
print(f"Secure File Path: {secure_file_path}")
