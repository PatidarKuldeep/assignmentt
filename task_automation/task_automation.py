import os

directory = "task_automation"
if not os.path.exists(directory):
    os.makedirs(directory)

file_names = ["file1.txt", "file2.txt", "file3.txt"]
for file_name in file_names:
    with open(os.path.join(directory, file_name), "w") as file:
        file.write("This is some sample content for " + file_name)

concatenated_content = ""
for file_name in file_names:
    with open(os.path.join(directory, file_name), "r") as file:
        concatenated_content += file.read()

with open(os.path.join(directory, "concatenated.txt"), "w") as file:
    file.write(concatenated_content)

print("Content of concatenated.txt:")
with open(os.path.join(directory, "concatenated.txt"), "r") as file:
    print(file.read())

for file_name in file_names:
    os.remove(os.path.join(directory, file_name))

print("Files deleted successfully.")
