import os

# 1. Create a directory named "task_automation" if it doesn't exist
directory = "task_automation"
if not os.path.exists(directory):
    os.makedirs(directory)

# 2. Inside the directory, create three text files with any content
file_names = ["file1.txt", "file2.txt", "file3.txt"]
for file_name in file_names:
    with open(os.path.join(directory, file_name), "w") as file:
        file.write("This is some sample content for " + file_name)

# 3. Concatenate the content of the three files into a new file named "concatenated.txt"
concatenated_content = ""
for file_name in file_names:
    with open(os.path.join(directory, file_name), "r") as file:
        concatenated_content += file.read()

# Write the concatenated content to a new file
with open(os.path.join(directory, "concatenated.txt"), "w") as file:
    file.write(concatenated_content)

# 4. Print the content of "concatenated.txt" to the console
print("Content of concatenated.txt:")
with open(os.path.join(directory, "concatenated.txt"), "r") as file:
    print(file.read())

# 5. Delete "file1.txt", "file2.txt", and "file3.txt" from the directory
for file_name in file_names:
    os.remove(os.path.join(directory, file_name))

print("Files deleted successfully.")
