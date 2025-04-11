import requests
import os
import shutil
from datetime import datetime

parent_dir = "/Users/verlock/workflows/gtp/week1"
dir_name = "ishmael_gyamfi"

if os.path.exists(dir_name):
    try:
        shutil.rmtree(dir_name)
        print(f"Directory '{dir_name}' has been removed successfully.")
    except Exception as e:
        print(f"Error: {e}")

full_path = os.path.join(parent_dir, dir_name)

#creating a directory
os.makedirs(full_path, exist_ok=True)
#cd in that directory
os.chdir(full_path)

print(os.getcwd())

if not os.path.exists(dir_name):
    os.makedirs(dir_name)
print(f"Directory: {dir_name} created.")

local_file_path = os.path.join(dir_name, "ishmael_gyamfi.txt")

url = "https://raw.githubusercontent.com/sdg000/pydevops_intro_lab/main/change_me.txt"

response = requests.get(url)
if response.status_code == 200:
    print(f"File successfully downloaded.")
    with open(local_file_path, "wb") as file:
        file.write(response.content)
        print('File saved successfully.')
else:
    print(f"Failed to download file. Status code: {response.status_code}")

user_input = input("Describe what you have learned so far in a sentence: ")
now = datetime.now()
current_time = now.strftime("%Y-%m-%d %H:%M:%S")

with open(local_file_path, "w") as file:
    file.write(user_input + "\n")
    file.write(f"Last modified on: {current_time}")
    print("File successfully modified.")

with open(local_file_path, "r") as file:
    print("\nYou Entered: ", end='')
    print(file.read())